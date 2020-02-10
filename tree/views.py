from django.shortcuts import render
from django.views.generic import ListView, DetailView
# Create your views here.

from tree.models import Tree

def detail_view(request, id):
    tree = Tree.objects.get(pk=id)
    template = "tree/detail.html"
    context = {"tree": tree}

    

    return render(request, template, context) 

class TreeListView(ListView):
    queryset = Tree.objects.all()
    template_name = "tree/list.html"
    

class TreeDetailView(DetailView):
    queryset = Tree.objects.all()
    template_name = "tree/detail.html"


    # def get_object(self):
    #     obj = super().get_object()
    #     print(obj)
    #     return obj

    def get_context_data(self, id=None, *args, **kwargs):
        context = super(TreeDetailView, self).get_context_data(**kwargs)
        return context


class TreeApprovedListView(ListView):
    """When user approved the client's tree, this function servers the approved ones"""
    queryset = Tree.objects.all()
    template_name = "tree/list-featured.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Tree.objects.approved()
    
    

class TreeApprovedDetailView(DetailView):
    template_name = "tree/detail.html"