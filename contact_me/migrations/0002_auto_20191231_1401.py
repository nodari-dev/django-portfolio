# Generated by Django 2.2.6 on 2019-12-31 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_me', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('text', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='UserMessage',
        ),
    ]