# Generated by Django 3.2.6 on 2021-09-22 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0052_personalmenu_instruction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dishitem',
            name='dish',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dish_items', to='grocery.personalmenu'),
        ),
    ]