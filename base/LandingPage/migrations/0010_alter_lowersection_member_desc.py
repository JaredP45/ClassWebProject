# Generated by Django 3.2.3 on 2022-03-16 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LandingPage', '0009_auto_20220315_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lowersection',
            name='member_desc',
            field=models.TextField(default='', max_length=750),
        ),
    ]
