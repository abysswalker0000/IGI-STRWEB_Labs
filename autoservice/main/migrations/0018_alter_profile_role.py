# Generated by Django 4.2.13 on 2024-05-31 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_profile_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[{'customer', 'Customer'}, {'Admin', 'admin'}, {'Worker', 'worker'}], default='idk', max_length=20),
        ),
    ]
