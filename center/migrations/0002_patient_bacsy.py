# Generated by Django 2.1.5 on 2019-04-07 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('center', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='bacsy',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='center.Bacsy'),
            preserve_default=False,
        ),
    ]
