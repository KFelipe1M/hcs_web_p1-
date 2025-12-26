import os
from django.shortcuts import render, redirect
from markdown2 import Markdown
from django import forms
from django.http import HttpResponse
from . import views
from django.http import Http404
from . import util
from random import randint


def md_to_html(title):
    content = util.get_entry(title)
    markdowner = Markdown()
    if content == None:
        return None
    else:
     return markdowner.convert("**test**")

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    content = util.get_entry(title)
    if content is None:
        return HttpResponseNotFound(f"<h1>Page '{title}' not found</h1>")
    
    
    markdowner = Markdown()
    content = markdowner.convert(content)
    return render(request, "encyclopedia/entry.html", {'content': content, 'title':title})

def search(request):
   q = request.GET.get('q').strip()
   if q in util.list_entries():
      return redirect("encyclopedia:entry", title=q)
   page=util.get_entry(q)
   if page is None:
      return render(request,"encyclopedia/error.html",{
      })
   return render(request,"encyclopedia/entry.html", {
      "entries": util.search(q), "q":q
      })

def random(reuest):
   entries = util.list_entries()
   entry = entries[randint(0, len(entries)-1)]
   return redirect("encyclopedia:entry", entry)


def index(request):
    return render(request, "encyclopedia.html")

def newentrymaker(request):

    if request.method == "GET":
        return render(request,"encyclopedia/entry.html")
        
    title = request.POST.get("title")
    content = request.POST.get("content")
    content_md = f"# {title}\n\n{content}"
    util.save_entry(title, content_md)
    
    return redirect("encyclopedia:index")

def edit(request, entry):

    if request.method == "GET":
        content = util.get_entry(entry)
        return render(request, "encyclopedia/editentry.html", {
        "title": entry,
        "content": content
        })
    
    title = request.POST.get("title")
    content = request.POST.get("content")
    content_md = f"# {title}\n\n{content}"
    util.save_entry(title, content_md)
    return redirect("encyclopedia:entry", entry)
