# Generated by Django 4.0.2 on 2022-02-24 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LandingPage', '0003_lowersection_member_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='midsection',
            name='meet_team',
            field=models.CharField(default='', max_length=250),
        ),
    ]
