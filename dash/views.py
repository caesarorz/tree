from django.shortcuts import render
# from django.contrib.auth.models import User
from accounts.models import User


# Create your views here.

def list_users(request):
    users = User.objects.all()
    template = 'dash/list_users.html'
    context = {'users': users}

    return render(request, template, context)