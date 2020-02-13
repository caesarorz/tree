import random
import os
from django.conf import settings
from django.urls import reverse
from django.db import models

User = settings.AUTH_USER_MODEL


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_filename = random.randint(1, 99999999)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(
        new_filename=new_filename, ext=ext)
    return "tree/{new_filename}/{final_filename}".format(
        new_filename=new_filename,
        final_filename=final_filename
    )


class TreeQuerySet(models.query.QuerySet):
    def approved(self):
        return self.filter(approved=True, active=True)

class TreeManager(models.Manager):

    def get_queryset(self):
        return TreeQuerySet(self.model, using=self._db)

    def approved(self):
        return self.get_queryset().approved()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None
    
class Tree(models.Model):
    title = models.CharField(max_length=120)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField()
    location = models.CharField(max_length=120)
    active = models.BooleanField(default=True)
    approved = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = TreeManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("tree_detail", kwargs={"pk": self.pk})


class TreeImage(models.Model):
    tree = models.ForeignKey(Tree, on_delete=models.CASCADE)
    # title = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)

    def __str__(self):
        return self.tree.title


    