# Generated by Django 2.2 on 2019-05-02 02:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('center', '0010_auto_20190502_0220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yeucau',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
