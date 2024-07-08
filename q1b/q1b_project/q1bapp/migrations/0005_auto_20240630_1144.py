# Generated by Django 3.2.25 on 2024-06-30 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('q1bapp', '0004_auto_20240629_1953'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='patient_group',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
