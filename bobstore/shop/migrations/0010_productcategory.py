# Generated by Django 3.2.18 on 2023-06-07 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_seller_storetype'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
            ],
        ),
    ]
