# Generated by Django 3.2.18 on 2023-05-20 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20230520_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.ImageField(upload_to='users/sellers/images/products/'),
        ),
        migrations.AlterField(
            model_name='seller',
            name='email',
            field=models.EmailField(default=None, max_length=254, null=True),
        ),
    ]
