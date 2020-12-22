from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def css(request):
    return render(request,"encyclopedia/css.html",{
        "content": util.get_entry("CSS")
    })
def django(request):
    return render(request,"encyclopedia/django.html",{
        "content": util.get_entry("Django")
    })
def git(request):
    return render(request,"encyclopedia/git.html",{
        "content": util.get_entry("Git")
    })
def html(request):
    return render(request,"encyclopedia/html.html",{
        "content": util.get_entry("HTML")
    })
def python(request):
    return render(request,"encyclopedia/python.html",{
        "content": util.get_entry("Python")
    })