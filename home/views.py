from django.shortcuts import render

# Create your views here.
from tree.models import Tree


def home_page(request):
    tree = Tree.objects.all().filter(approved=True)
    context = {
        "tree_card":tree
        }
    template = "home_page.html"
    return render(request, template, context)