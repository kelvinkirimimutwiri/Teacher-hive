# Generated by Django 4.2.6 on 2023-10-08 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
