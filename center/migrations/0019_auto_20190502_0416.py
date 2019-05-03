# Generated by Django 2.2 on 2019-05-02 04:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('center', '0018_auto_20190502_0412'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='yeucau',
            name='id',
        ),
        migrations.AlterField(
            model_name='yeucau',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='+', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
