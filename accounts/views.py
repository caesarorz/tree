from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.utils.http import is_safe_url
from django.utils.safestring import mark_safe
from django.http import HttpResponse, JsonResponse
import json
# from .signals import user_logged_in

from .forms import LoginForm, RegisterForm


def login_account(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if request.is_ajax():
            perm = False
            if user is not None:
                login(request, user)
            if request.user.is_authenticated:
                perm = True
            data = {
                "permission": perm,
            }
            return JsonResponse(data)
    error = {"error": "error"}
    
    print(form.errors)
    print(form.non_field_errors)
    # print(form.errors)

    return JsonResponse(error) 


User = get_user_model()
def register(request):
    form = RegisterForm(request.POST or None)
    email = request.POST.get("email", None)

    print("register user, email ", email)
    print("form", form)
    if form.is_valid():
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = User.objects.create_user(email, password)
        perm = False
        if user is not None:
            if request.is_ajax():
                perm = True
                data = {
                    "permission": perm,
                }
            return JsonResponse(data)

    print("errors ", form.errors)
    # print(form.non_field_errors)
    error = {"error": form.errors}
    # print(form.errors)

    return JsonResponse(error) 