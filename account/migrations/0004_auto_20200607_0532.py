# Generated by Django 3.0.6 on 2020-06-07 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20200607_0528'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='selectedtheme',
            unique_together={('theme', 'user')},
        ),
    ]
