# Generated by Django 3.2.6 on 2021-08-21 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0037_auto_20210821_1728'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userpost',
            name='user_id',
        ),
        migrations.AddField(
            model_name='userpost',
            name='user_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
