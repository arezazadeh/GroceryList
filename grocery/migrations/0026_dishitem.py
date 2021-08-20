# Generated by Django 3.2.6 on 2021-08-14 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0025_remove_groceryitem_dish'),
    ]

    operations = [
        migrations.CreateModel(
            name='DishItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=255, null=True)),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grocery.personalmenu')),
            ],
        ),
    ]