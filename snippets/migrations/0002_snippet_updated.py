# Generated by Django 4.1.4 on 2023-01-11 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
