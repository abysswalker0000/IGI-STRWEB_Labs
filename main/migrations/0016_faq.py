# Generated by Django 4.2.13 on 2024-05-31 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_news_contacts_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('answer', models.TextField()),
                ('answer_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
