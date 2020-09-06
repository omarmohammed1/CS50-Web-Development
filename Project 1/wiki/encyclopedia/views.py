from django.shortcuts import render

from . import util
import markdown2 as md


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entrypage(request, entry_name):
    return render(request, "encyclopedia/entrypage.html", {
        "encyclopedia_page_name" : entry_name.capitalize(),
        "encyclopedia_page_block": md.markdown(util.get_entry(entry_name))

    })