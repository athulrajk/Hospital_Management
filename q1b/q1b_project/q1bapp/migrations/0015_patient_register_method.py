# Generated by Django 3.2.25 on 2024-07-02 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('q1bapp', '0014_alter_eventappointment_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='register_method',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
    ]
