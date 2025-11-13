from django.shortcuts import render
import Markdown2
from markdown2 import Markdown
from . import util


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
   html_content = md_to_html(title)
   if html_content == None:
      return render(request, "encyclopedia/errorm.html")
   else:
      return render(request, "newentry/newentrymaker.html")