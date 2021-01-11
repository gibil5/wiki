"""
Module Views
    Created:    28 dec 2020
    Last up:    11 jan 2021

Interface:
    index
    search
    wiki
    create
    edit
    update

Try and catch
    try:
        entry = util.get_entry(title=title)
    except FileNotFoundError:
        print('\nERROR')
    else:
        print('\nSUCCESS')
"""
from markdown2 import Markdown
from django.shortcuts import render
from django import forms
from django.forms import ModelForm
from .models import Page
from . import util
from . import lib as x

SUCCESS = '\nSUCCESS'
ERROR = '\nERROR'

PAGE_NOT_FOUND = 'The requested page was not found.'

class PageForm(ModelForm):
    """
    Page form
    """
    class Meta:
        """
        Meta
        """
        model = Page
        fields = ['title', 'content']
    title = forms.CharField(label="Title")
    content = forms.CharField(label="Content", widget=forms.Textarea(attrs={}))


class NewPageForm(forms.Form):
    """
    New Page form
    """
    title = forms.CharField(label="Title")
    content = forms.CharField(label="Content", widget=forms.Textarea(attrs={}))


def index(request):
    """
    Index
    """
    x.printx('*** index')
    return render(request, "encyclopedia/index.html",
        {
            "entries": util.list_entries()
        })

def search(request):
    '''
    Search
    '''
    x.printx('*** search')
    title = request.GET.get('q', '')

    # Try and catch
    try:
        entry = util.get_entry(title=title)
    except FileNotFoundError:
        x.printx(ERROR)
        titles = []
        titles = util.is_subtring(query=title, x_list=util.list_entries())
        if titles:
            return render(request, "encyclopedia/warning.html", {
                "entries": titles,
                "message": 'It might be here.'
            })
        else:
            return render(request, "encyclopedia/error.html", {
                "message": PAGE_NOT_FOUND,
            })
    else:
        x.printx(SUCCESS)
        markdowner = Markdown()
        html = markdowner.convert(entry)
        return render(request, "encyclopedia/wiki.html", {
            "html": html,
            "page": title,
        })



def wiki(request, title):
    """
    Req: /wiki/<page>/
    """
    x.printx('*** wiki')

    # Try and catch
    try:
        entry = util.get_entry(title=title)
    except FileNotFoundError:
        x.printx(ERROR)
        return render(request, "encyclopedia/error.html", {
            "message": PAGE_NOT_FOUND,
        })
    else:
        x.printx(SUCCESS)
        markdowner = Markdown()
        html = markdowner.convert(entry)
        return render(request, "encyclopedia/wiki.html", {
            "html": html,
            "page": title,
        })


def create(request):
    """
    Create
    """
    x.printx('*** create')

    if request.method == 'POST':
        form = NewPageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            x.printx('form IS valid')

            # Try and catch
            try:
                entry = util.get_entry(title=title)
            except FileNotFoundError:
                x.printx(ERROR)
                x.printx('Entry is created')
                util.save_entry(title=title, content=content)
                entry = util.get_entry(title=title)
                markdowner = Markdown()
                html = markdowner.convert(entry)
                return render(request, "encyclopedia/wiki.html", {
                    "html": html,
                    "page": entry,
                })
            else:
                x.printx(SUCCESS)
                x.printx('Entry already exists')
                return render(request, "encyclopedia/error.html", {
                    "message": 'Entry already exists !'
                })

        else:
            x.printx('form is NOT valid')
            return render(request, "encyclopedia/error.html", {
                "message": 'Form is not valid !'
            })
    else:
        x.printx('New form')
        return render(request, "encyclopedia/create.html", {
            "form": NewPageForm(),
        })


def edit(request, page):
    """
    Edit
    """
    x.printx('*** edit')

    if request.method == 'GET':
        #print('get')
        x.printx('** get')
        title = page

        # Try and catch
        try:
            entry = util.get_entry(title=title)
            content = entry
        except FileNotFoundError:
            x.printx(ERROR)
            return render(request, "encyclopedia/error.html", {
                "message": PAGE_NOT_FOUND,
            })
        else:
            x.printx(SUCCESS)
            obj = Page(title=title, content=content, name=title)
            form = PageForm(instance=obj)
            return render(request, "encyclopedia/edit.html", {
                "form": form,
            })

    elif request.method == 'POST':
        x.printx('** post')
        print('This should never happen !')


def update(request):
    """
    update
    """
    x.printx('*** update')
    x.printx(request)
    x.printx(request.POST)

    if request.method == 'POST':
        x.printx('post')
        form = NewPageForm(request.POST)

        if form.is_valid():
            x.printx('form IS valid')
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            x.printx(f'Title: {title}')
            x.printx(f'Content: {content}')
            util.save_entry(title=title, content=content)

            # Try and catch
            try:
                entry = util.get_entry(title=title)
            except FileNotFoundError:
                x.printx(ERROR)
                return render(request, "encyclopedia/error.html", {
                    "message": PAGE_NOT_FOUND,
                })
            else:
                x.printx(SUCCESS)
                markdowner = Markdown()
                html = markdowner.convert(entry)
                return render(request, "encyclopedia/wiki.html", {
                    "html": html,
                    "page": entry,
                })

        else:
            x.printx('form not valid')
            return render(request, "encyclopedia/error.html", {
                "message": 'Form is not valid !'
            })

    elif request.method == 'GET':
        print('get')
        print('This should not happen !')
