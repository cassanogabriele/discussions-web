# Generated by Django 5.0 on 2023-12-06 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0005_alter_entry_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]