# Generated by Django 5.1.2 on 2024-10-23 07:59

import FrutipediaApp.fruits.validators
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fruit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(error_messages={'unique': 'This fruit name is already in use! Try a new one.'}, max_length=30, unique=True, validators=[django.core.validators.MinLengthValidator(2), FrutipediaApp.fruits.validators.OnlyLetterValidator()])),
                ('image_url', models.URLField()),
                ('description', models.TextField()),
                ('nutrition', models.TextField(blank=True, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fruits', to='profiles.profile')),
            ],
        ),
    ]
