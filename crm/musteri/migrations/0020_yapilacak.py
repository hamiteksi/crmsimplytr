# Generated by Django 4.1.7 on 2023-07-25 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musteri', '0019_alter_customer_application_number_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Yapilacak',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yapilacak', models.CharField(max_length=255)),
                ('detay', models.TextField()),
                ('olusturulma_tarihi', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
