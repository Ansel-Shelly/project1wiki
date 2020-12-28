from django.shortcuts import render

from . import util

import markdown2

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def site(request, site):
    if util.get_entry(site):
        content = markdown2.markdown(util.get_entry(site))
    else:
        content = None
    return render(request, "encyclopedia/site.html", {
        "site": site,  
        "content": content
    })
