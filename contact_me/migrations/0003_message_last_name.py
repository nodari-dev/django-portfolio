# Generated by Django 2.2.6 on 2019-12-31 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_me', '0002_auto_20191231_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='last_name',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
