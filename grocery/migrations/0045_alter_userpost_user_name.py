# Generated by Django 3.2.6 on 2021-09-11 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0044_alter_userpost_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpost',
            name='user_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]