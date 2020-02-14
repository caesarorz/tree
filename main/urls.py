"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView

from home.views import home_page
from tree.views import (detail_view, 
                        TreeListView, 
                        TreeDetailView, 
                        TreeApprovedListView, 
                        tree_user,
                        upload,
                        upload_image,
                        delete_image_tree,
                        )
from aboutus.views import about
from dash.views import list_users


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home_page'),
    path('account/', include('accounts.urls')),
    path('about/', about, name='about_page'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('tree-user/', tree_user, name='tree_user'),
    path('detail/<int:pk>/', TreeDetailView.as_view(), name='tree_detail'),
    path('approved-list/', TreeApprovedListView.as_view()),
    path('list/', TreeListView.as_view()),
    path('upload/', upload, name='upload'),
    path('upload-image-tree/', upload_image, name='upload_image_tree'),
    path('delete-image-tree/', delete_image_tree, name='delete_image_tree'),
    path('users/', list_users, name='list_users'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    