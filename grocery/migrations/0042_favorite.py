# Generated by Django 3.2.6 on 2021-09-07 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0041_auto_20210822_1628'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=255, null=True)),
                ('user_id', models.IntegerField(null=True)),
            ],
        ),
    ]
