# Generated by Django 5.0.6 on 2024-05-16 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('text', models.TextField(max_length=255)),
                ('published_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
