"""
Module Util
    Created:    28 dec 2020
    Last up:     4 jan 2021

Library for interaction with MD files

Interface:
    - list_entries()
    - get_entry(title)
    - save_entry(title, content)
    - delete_entry(title)
    - is_subtring(query, x_list)
    - print_response(response)
    - parse_inputs(html, tag, name)
"""
import re
from bs4 import BeautifulSoup
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

# ------------------------------------------------------------------------------
#                              Entries
# ------------------------------------------------------------------------------
def list_entries():
    """
    Returns a list of all names of encyclopedia entries.
    """
    _, filenames = default_storage.listdir("entries")
    #return list(sorted(re.sub(r"\.md$", "", filename) for filename in filenames if filename.endswith(".md")))
    arr = []
    for filename in filenames:
        if filename.endswith(".md"):
            arr.append(re.sub(r"\.md$", "", filename))
    return list(sorted(arr))


def get_entry(title):
    """
    Retrieves an encyclopedia entry by its title. 
    If no such entry exists, the function returns None.
    """
    #try:
    #    f = default_storage.open(f"entries/{title}.md")
    #    return f.read().decode("utf-8")
    #except FileNotFoundError:
    #    return None
    try:
        f = default_storage.open(f"entries/{title}.md")
        return f.read().decode("utf-8")
    except FileNotFoundError as e:
        raise FileNotFoundError('File not found')


def save_entry(title, content):
    """
    Saves an encyclopedia entry, given its title and Markdown content.
    If an existing entry with the same title already exists,it is replaced.
    """
    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)

    #default_storage.save(filename, ContentFile(content))
    content_file = f'#{title}\n\n{content}'
    default_storage.save(filename, ContentFile(content_file))


def delete_entry(title):
    """
    Deletes an encyclopedia entry, given its title.
    """
    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)


def is_subtring(query, x_list):
    """
    Is substring
    """
    query = query.lower()
    x_list = [x.lower() for x in x_list]
    titles = []
    for title in x_list:
        if query in title:
            titles.append(title)
    if titles:
        return titles
    else:
        return None

# ------------------------------------------------------------------------------
#                              Utilities
# ------------------------------------------------------------------------------
def print_response(response):
    """
    Print response
    """
    print(f"\nThe Response is:\n{response}", )
    print(f"\nThe Client is:\n{response.client}", )
    print(f"\nThe Status code is:\n{response.status_code}", )
    print(f"\nThe Content is:\n{response.content}", )
    #print(f"\n\nThe Context is:\n\n{response.context}", )
    print(f"\nThe exc_info is:\n{response.exc_info}", )
    #print(f"\nThe json is:\n{response.json()['name']}", )
    print(f"\nThe request is:\n{response.request}", )
    print(f"\nThe template is:\n{response.templates}", )
    print(f"\nThe resolver_match is:\n{response.resolver_match}", )
    #print(f"\nThe text is:\n{response.text}", )


def parse_title(html):
    """
    Parse title
    """
    #html = str(response.content)
    parsed_html = BeautifulSoup(html, features="html.parser")
    #print(parsed_html.body.find('div', attrs={'class':'container'}).text)

    #if (out := parsed_html.body.find('h1', attrs={})):
    if (out := parsed_html.body.find('h1', attrs={})) != None:
        return out.text
    #else:
    #    return None
    return None


def parse_inputs(html, tag, name):
    """
    Parse inputs
    """
    parsed_html = BeautifulSoup(html, features="html.parser")

    #print(parsed_html.body.find('div', attrs={'class':'container'}).text)
    #print(parsed_html.body.find('input', attrs={'class':'container'}).text)
    #out = parsed_html.body.find('input', attrs={}).text
    out = parsed_html.body.find(tag, attrs={'name':name})
    return out

    #if (out := parsed_html.body.find('h1', attrs={})) != None:
    #    return out.text
    #else:
    #    return None



