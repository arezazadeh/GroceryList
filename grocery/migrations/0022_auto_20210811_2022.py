# Generated by Django 3.2.6 on 2021-08-11 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0021_alter_grocerylist_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grocerylist',
            name='date',
        ),
        migrations.AlterField(
            model_name='grocerylistarchive',
            name='date',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
