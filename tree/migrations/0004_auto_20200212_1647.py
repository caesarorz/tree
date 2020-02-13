# Generated by Django 2.2.3 on 2020-02-12 16:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0003_auto_20200212_1642'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='treeimage',
            name='tree_obj',
        ),
        migrations.AddField(
            model_name='treeimage',
            name='tree',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tree.Tree'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tree',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]