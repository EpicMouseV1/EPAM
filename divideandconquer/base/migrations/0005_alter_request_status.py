# Generated by Django 4.2 on 2023-04-16 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_request_close_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='status',
            field=models.CharField(choices=[('opt', 'new'), ('opt2', 'in progress'), ('opt3', 'completed')], default='opt', max_length=30),
        ),
    ]