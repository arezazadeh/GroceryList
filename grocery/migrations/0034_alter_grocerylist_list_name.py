# Generated by Django 3.2.6 on 2021-08-17 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0033_grocerylist_list_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grocerylist',
            name='list_name',
            field=models.CharField(default=1, max_length=255, null=True),
        ),
    ]
