from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.core.files.storage import FileSystemStorage
from django.conf import settings
# Create your views here.

from tree.models import Tree, TreeImage
from .forms import TreeImageForm

User = settings.AUTH_USER_MODEL

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


def tree_user(request):
    template = "tree/user-detail.html"
    context = {}
    return render(request, template, context)


def delete_image_tree(request):
    """Delete any image if neccesary"""
    context = {}
    template = "tree/create-tree.html"
    if request.user.is_authenticated and request.method == "POST":
        image_id = request.POST.get('image_id')
        if image_id:
            qs_image = TreeImage.objects.all().filter(id=image_id)
            qs_image.delete()
            redirect('upload')
    return render(request, template, context)

def upload_image(request):
    """After creating the Tree information (upload function), upload images"""
    context = {}
    template = "tree/create-tree.html" 
    if request.user.is_authenticated and request.method == "POST":   
        tree_of_user = Tree.objects.filter(user=request.user)  
        tree_image = None
        print("uploading image")
        if request.FILES and tree_of_user.exists():
            tree_image = request.FILES['image']
            try: 
                tree_of_user = tree_of_user.first()
                new_image_tree = tree_of_user.treeimage_set.create(image=tree_image)
                new_image_tree.save()
                print("#################### new_image.id ", new_image.id)
                return redirect('upload')
            except: 
                # raise error("error")
                pass
    return redirect('upload')
                

def upload(request):
    """Creating the tree information, title, description, location (GPS)"""
    context = {}
    template = "tree/create-tree.html"
    if request.user.is_authenticated:     
        if request.method == "POST":
            tree_title = request.POST.get('title')
            tree_description = request.POST.get('description')
            tree_location = request.POST.get('location')
            tree_user = request.user
            tree_of_user = Tree.objects.filter(user=request.user)
            treeForm = TreeImageForm(request.POST)
            if tree_of_user.exists():
                print("Yess", tree_of_user)
            else:
                print("Nopp")
                new_tree = Tree.objects.create(
                    title=tree_title, 
                    user=tree_user,
                    description=tree_description,
                    location=tree_location
                    )
                print("new_tree ", new_tree, type(new_tree))
                new_tree.save()
                return redirect('upload')
    return render(request, template, context)
