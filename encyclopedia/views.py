from django.shortcuts import render, redirect
from markdown2 import Markdown
from . import views
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
    return render(request, "entrymaker/entry.html", {'content': content, 'title':title})

def search(request):
   q = request.GET.get('q').strip()
   if q in util.list_entries():
      return redirect("encyclopedia:entry", title=q)
   return render(request,"encyclopedia/entry.html", {
      "entries": util.search(q), "q":q
      })
