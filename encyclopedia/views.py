"""
Module Views
    Created:    28 dec 2020
    Last up:     6 jan 2021

Interface:
    - index
    - search
    - wiki
    - create
    - edit

Do Pythonic coding
"""
from markdown2 import Markdown
from django.shortcuts import render
#from django.utils.safestring import mark_safe
#from django.http import HttpResponse, HttpResponseRedirect
#from django.urls import reverse
from django import forms
from django.forms import ModelForm
from . import util
from .models import Page

#VERBOSE = 1
VERBOSE = 0

class PageForm(ModelForm):
    """
    Page form
    """
    class Meta:
        """
        Meta
        """
        model = Page
        #fields = ['name', 'title', 'content']
        fields = ['title', 'content']
    title = forms.CharField(label="Title")
    content = forms.CharField(label="Content", widget=forms.Textarea(attrs={}))


class NewPageForm(forms.Form):
    """
    New Page form
    """
    title = forms.CharField(label="Title")
    content = forms.CharField(label="Content", widget=forms.Textarea(attrs={}))
    #sender = forms.EmailField()
    #cc_myself = forms.BooleanField(required=False)


def index(request):
    """
    Index
    """
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
    query = request.GET.get('q', '')
    try:
        entry = util.get_entry(query)

    except FileNotFoundError:
        #print('\nERROR')
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
        #print('\nSUCCESS')
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
    #print('wiki')
    #print(request)
    #print(page)
    try:
        entry = util.get_entry(page)
    except FileNotFoundError:
        #print('\nERROR')
        return render(request, "encyclopedia/error.html", {
            "message": 'The requested page was not found.',
        })
    else:
        #print('\nSUCCESS')
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
    #print('\n*** create')
    #print(request)

    if request.method == 'POST':
        form = NewPageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            #print('form IS valid')
            #print(f'Title: {title}')
            #print(f'Content: {content}')

            try:
                entry = util.get_entry(title)
            except FileNotFoundError:
                #print('\nERROR')
                #print('Entry is created')
                util.save_entry(title, content)
                entry = util.get_entry(title)
                markdowner = Markdown()
                html = markdowner.convert(entry)
                return render(request, "encyclopedia/wiki.html", {
                    "html": html,
                    "page": entry,
                })
            else:
                #print('\nSUCCESS')
                #print('Entry already exists')
                return render(request, "encyclopedia/error.html", {
                    "message": 'Entry already exists !'
                })
        else:
            #print('form is NOT valid')
            return render(request, "encyclopedia/error.html", {
                "message": 'Form is not valid !'
            })
    else:
        #print('New form')
        return render(request, "encyclopedia/create.html", {
            "form": NewPageForm(),
        })




def edit(request, page):
    """
    Edit
    """
    print('*** edit')
    print(request)
    print(page)
    query = request.POST.get('q', '')
    print(query)

    if request.method == 'GET':
        print('get')

        title = page
        content = util.get_entry(title)

        #obj = Page.objects.get(name=page.lower())
        obj = Page(title=title, content=content, name=title)
        form = PageForm(instance=obj)

        return render(request, "encyclopedia/edit.html", {
            "form": form,
        })

    # This never happens !
    #if request.method == 'POST':
    #    1/0
    #    print('post')
    #    form = NewPageForm(request.POST)
    #    if form.is_valid():
    #        title = form.cleaned_data["title"]
    #        content = form.cleaned_data["content"]
    #        if VERBOSE:
    #            print('form IS valid')
    #            print(f'Title: {title}')
    #            print(f'Content: {content}')
    #        return render(request, "encyclopedia/error.html", {
    #            "message": 'In progress...'
    #        })
    #    else:
    #        print('form not valid')
    #        return render(request, "encyclopedia/error.html", {
    #            "message": 'In progress...'
    #        })
    #else:


def update(request):
    """
    update
    """
    print('*** update')
    print(request)
    print(request.POST)

    if request.method == 'POST':
        print('post')

        form = NewPageForm(request.POST)

        if form.is_valid():
            print('form IS valid')

            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]

            print(f'Title: {title}')
            print(f'Content: {content}')

            util.save_entry(title, content)

            entry = util.get_entry(title)
            markdowner = Markdown()
            html = markdowner.convert(entry)

            return render(request, "encyclopedia/wiki.html", {
                "html": html,
                "page": entry,
            })

            #return render(request, "encyclopedia/error.html", {
            #    "message": 'Form is valid.'
            #})

        else:
            print('form not valid')
            return render(request, "encyclopedia/error.html", {
                "message": 'Form is NOT valid.'
            })

    #if request.method == 'POST':
    else:
        print('get')
