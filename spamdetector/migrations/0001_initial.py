# Generated by Django 4.2.1 on 2023-11-17 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.EmailField(max_length=254, unique=True)),
                ('is_phishing', models.BooleanField(default=False)),
            ],
        ),
    ]
