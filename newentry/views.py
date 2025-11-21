import os
from django.shortcuts import render, redirect
from markdown2 import Markdown
from django.conf import settings
from django.http import HttpResponse
from django.utils.text import slugify
from encyclopedia import util

def index(request):
    return render(request, "entrymaker/index.html")

def newentrymaker(request):

    if request.method == "GET":
        return render(request,"entrymaker/newentrymaker.html")
        
    title = request.POST.get("title")
    content = request.POST.get("content")
    content_md = f"# {title}\n\n{content}"
    util.save_entry(title, content_md)
    
    return redirect("encyclopedia:index")

def entry(request, title):
    content = util.get_entry(title)
    if content is None:
        content = "Page not faund"
    markdowner = Markdown()
    content = markdowner.convert(content)
    return render(request, "entrymaker/entry.html", {'content': content, 'title':title})