# Generated by Django 4.1.7 on 2023-05-29 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musteri', '0002_customer_payment_made_customer_phone_number_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Communication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('method', models.CharField(max_length=100)),
                ('details', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='communication_history',
            field=models.ManyToManyField(blank=True, to='musteri.communication'),
        ),
    ]
