from django.contrib import admin
from .models import Tree, TreeImage


class TreeImageInline(admin.TabularInline):
    model = TreeImage
    extra = 0
    max_num = 3
    fields = ('image',)

class TreeAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'user']
    inlines = [TreeImageInline]

    class Meta:
        model = Tree


admin.site.register(Tree, TreeAdmin)