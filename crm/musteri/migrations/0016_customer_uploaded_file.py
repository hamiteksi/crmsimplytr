# Generated by Django 4.1.7 on 2023-07-23 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musteri', '0015_alter_country_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='uploaded_file',
            field=models.FileField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
