# Generated by Django 4.2.6 on 2023-10-15 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='application_area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shop.applicationarea'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shop.category'),
        ),
    ]
