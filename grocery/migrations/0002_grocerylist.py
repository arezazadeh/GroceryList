# Generated by Django 3.1.4 on 2021-08-02 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroceryList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]
