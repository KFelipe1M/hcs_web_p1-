from django.shortcuts import render
from markdown2 import Markdown
from encyclopedia import util

def index(request):
    return render(request, "entrymaker/index.html")

def newentrymaker(request):
    return render(request,"entrymaker/newentrymaker.html")