# Generated by Django 2.2 on 2019-05-01 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('center', '0008_remove_user0_gioitinh'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yeucau',
            name='bs',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='center.Bacsy'),
        ),
    ]
