# Generated by Django 4.1.7 on 2023-07-14 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musteri', '0007_customer_mail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='mail',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
