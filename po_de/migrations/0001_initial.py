# Generated by Django 5.1.4 on 2024-12-11 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tille', models.CharField(max_length=200)),
                ('comment', models.TextField()),
                ('author', models.TextField()),
            ],
        ),
    ]
