# Generated by Django 3.2.9 on 2021-12-22 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_rename_pricepernight_home_pricepermonth'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='Photofile1',
            field=models.ImageField(blank=True, null=True, upload_to='assets/uploadedimg'),
        ),
        migrations.AddField(
            model_name='home',
            name='Photofile2',
            field=models.ImageField(blank=True, null=True, upload_to='assets/uploadedimg'),
        ),
        migrations.AddField(
            model_name='home',
            name='Photofile3',
            field=models.ImageField(blank=True, null=True, upload_to='assets/uploadedimg'),
        ),
        migrations.AddField(
            model_name='home',
            name='Photofile4',
            field=models.ImageField(blank=True, null=True, upload_to='assets/uploadedimg'),
        ),
        migrations.DeleteModel(
            name='HomeImgs',
        ),
    ]
