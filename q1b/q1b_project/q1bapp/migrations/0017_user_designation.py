# Generated by Django 3.2.25 on 2024-07-06 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('q1bapp', '0016_user_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='designation',
            field=models.CharField(blank=True, max_length=155, null=True),
        ),
    ]
