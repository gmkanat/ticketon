# Generated by Django 4.1.3 on 2022-12-26 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketprice',
            name='price',
            field=models.IntegerField(default=0, verbose_name='Price'),
        ),
    ]
