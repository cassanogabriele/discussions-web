# Generated by Django 2.2.3 on 2019-07-16 15:26

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('entries', '0003_auto_20190716_1726'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Person',
            new_name='Entry',
        ),
    ]
