'''
Module Util Db
    Created:     3 jan 2021
    Last up:     3 Jan 2021

Library for interaction with:
    MD files
    Page objects
    
Interface:
    list_entries()
    save_entry(title, content)
    get_entry(title)
'''
#import re
#from django.core.files.base import ContentFile
#from django.core.files.storage import default_storage
from .models import Page

# ------------------------------------------------------------------------------
#                              Pages
# ------------------------------------------------------------------------------
def delete_page(name):
    """
    Deletes an encyclopedia page, given its title and conent.
    """
    #print('\n\ndelete_page')
    #print(name)
    count = Page.objects.filter(name=name).count()
    #print(count)
    if count != 0:
        #print('jx')
        #page = Page(name=name, title=title, content=content)
        page = Page.objects.get(name=name)
        page.delete()
        #page.save()
        return page
    else:
        #print('jx 2')
        return None

def create_page(name, title, content):
    """
    Creates an encyclopedia page, given its title and conent.
    """
    count = Page.objects.filter(name=name).count()
    if count == 0:
        page = Page(name=name, title=title, content=content)
        page.save()
        return page
    else:
        return None


