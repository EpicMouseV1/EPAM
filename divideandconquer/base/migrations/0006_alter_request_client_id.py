# Generated by Django 4.2 on 2023-04-16 05:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_request_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='client_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.client'),
        ),
    ]