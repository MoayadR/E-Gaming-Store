# Generated by Django 4.2.5 on 2023-09-29 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_region_alter_product_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='ProductImages/'),
        ),
    ]