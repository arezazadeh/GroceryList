# Generated by Django 3.2.6 on 2021-08-21 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0039_userpost_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercomments',
            name='user_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='usercomments',
            name='date',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
