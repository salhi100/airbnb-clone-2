# Generated by Django 2.2.5 on 2019-11-03 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20191101_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('female', 'Female'), ('male', 'Male'), ('other', 'Other')], max_length=10),
        ),
    ]
