# Generated by Django 2.2 on 2019-05-01 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('center', '0006_loggeduser'),
    ]

    operations = [
        migrations.AddField(
            model_name='loggeduser',
            name='tp',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Thành phố:'),
        ),
    ]
