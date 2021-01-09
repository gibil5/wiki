"""
Module Views
    Created:    28 dec 2020
    Last up:     8 jan 2021

Interface:
    index
    search
    wiki
    create
    edit
    update
"""
from markdown2 import Markdown
from django.shortcuts import render
from django import forms
from django.forms import ModelForm
from .models import Page
from . import util
from . import lib as x

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

    try:
        entry = util.get_entry(page)
    except FileNotFoundError:
        print('\nERROR')
    else:
        print('\nSUCCESS')
    '''
    x.printx('*** search')
    query = request.GET.get('q', '')
    try:
        entry = util.get_entry(query)

    except FileNotFoundError:
        x.printx('\nERROR')
        titles = []
        titles = util.is_subtring(query, util.list_entries())
        if titles:
            return render(request, "encyclopedia/warning.html", {
                "entries": titles,
                "message": 'It might be here.'
            })
        else:
            return render(request, "encyclopedia/error.html", {
                "message": 'The requested page was not found.',
            })

    else:
        x.printx('\nSUCCESS')
        markdowner = Markdown()
        html = markdowner.convert(entry)
        return render(request, "encyclopedia/wiki.html", {
            "html": html,
            "page": query,
        })



def wiki(request, page):
    """
    Req: /wiki/<page>/

    try:
        entry = util.get_entry(page)
    except FileNotFoundError:
        print('\nERROR')
    else:
        print('\nSUCCESS')
    """
    x.printx('*** wiki')
    try:
        entry = util.get_entry(page)
    except FileNotFoundError:
        x.printx('\nERROR')
        return render(request, "encyclopedia/error.html", {
            "message": 'The requested page was not found.',
        })
    else:
        x.printx('\nSUCCESS')
        markdowner = Markdown()
        html = markdowner.convert(entry)
        return render(request, "encyclopedia/wiki.html", {
            "html": html,
            "page": page,
        })


def create(request):
    """
    Create

    try:
        entry = util.get_entry(page)
    except FileNotFoundError:
        print('\nERROR')
    else:
        print('\nSUCCESS')
    """
    x.printx('*** create')

    if request.method == 'POST':
        form = NewPageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            x.printx('form IS valid')

            try:
                entry = util.get_entry(title)
            except FileNotFoundError:
                x.printx('\nERROR')
                x.printx('Entry is created')
                util.save_entry(title, content)
                entry = util.get_entry(title)
                markdowner = Markdown()
                html = markdowner.convert(entry)
                return render(request, "encyclopedia/wiki.html", {
                    "html": html,
                    "page": entry,
                })
            else:
                x.printx('\nSUCCESS')
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
    #print(request)
    #print(page)
    query = request.POST.get('q', '')
    #print(query)

    if request.method == 'GET':
        #print('get')
        x.printx('** get')
        title = page

        try:
            entry = util.get_entry(title)
            content = entry
        except FileNotFoundError:
            x.printx('\nERROR')
            return render(request, "encyclopedia/error.html", {
                "message": 'The requested page was not found.',
            })
        else:
            x.printx('\nSUCCESS')
            obj = Page(title=title, content=content, name=title)
            form = PageForm(instance=obj)
            return render(request, "encyclopedia/edit.html", {
                "form": form,
            })
        #content = util.get_entry(title)

    else:
        x.printx('** post')
        print('This should not happen !')
        raise ThisShouldNotHappen('This should not happen')



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
            util.save_entry(title, content)

            try:
                entry = util.get_entry(title)
            except FileNotFoundError:
                x.printx('\nERROR')
                return render(request, "encyclopedia/error.html", {
                    "message": 'The requested page was not found.',
                })
            else:
                x.printx('\nSUCCESS')
                markdowner = Markdown()
                html = markdowner.convert(entry)
                return render(request, "encyclopedia/wiki.html", {
                    "html": html,
                    "page": entry,
                })
            #entry = util.get_entry(title)

        else:
            x.printx('form not valid')
            return render(request, "encyclopedia/error.html", {
                "message": 'Form is not valid !'
            })

    else:
        print('get')
        print('This should not happen !')
        raise ThisShouldNotHappen('This should not happen')
