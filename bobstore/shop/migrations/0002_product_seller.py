# Generated by Django 3.2.18 on 2023-05-19 19:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('profile_pic', models.ImageField(upload_to='users/sellers/images/profiles')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='sellers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('amount', models.IntegerField()),
                ('price', models.FloatField()),
                ('picture', models.ImageField(upload_to='users/sellers/images/products')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sellers', to='shop.seller')),
            ],
        ),
    ]
