# Generated by Django 4.1.7 on 2023-07-25 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musteri', '0022_yapilacak_tamamlandi'),
    ]

    operations = [
        migrations.AddField(
            model_name='yapilacak',
            name='tamamlanma_tarihi',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
