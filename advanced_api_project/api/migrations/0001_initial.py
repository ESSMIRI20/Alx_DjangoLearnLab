# Generated by Django 5.1.2 on 2024-12-10 14:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the author', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title of the book', max_length=200)),
                ('publication_year', models.IntegerField(help_text='Year the book was published')),
                ('author', models.ForeignKey(help_text='Author of the book', on_delete=django.db.models.deletion.CASCADE, related_name='books', to='api.author')),
            ],
        ),
    ]
