# Generated by Django 2.2 on 2019-05-02 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('center', '0021_auto_20190502_0509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yeucau',
            name='bs',
            field=models.CharField(blank=True, default='', max_length=20, null=True, verbose_name='bacsy'),
        ),
    ]
