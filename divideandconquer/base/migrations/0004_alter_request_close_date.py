# Generated by Django 4.2 on 2023-04-16 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_myuser_managers_alter_myuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='close_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
