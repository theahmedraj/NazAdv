# Generated by Django 2.1.2 on 2020-04-26 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_service_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service_body',
            name='summary',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='service_header',
            name='summary',
            field=models.TextField(),
        ),
    ]
