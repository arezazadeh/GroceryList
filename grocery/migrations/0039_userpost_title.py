# Generated by Django 3.2.6 on 2021-08-21 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0038_auto_20210821_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpost',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
