# Generated by Django 3.2.6 on 2021-08-14 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0028_remove_dishitem_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
            ],
        ),
    ]
