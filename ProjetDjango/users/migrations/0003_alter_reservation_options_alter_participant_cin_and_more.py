# Generated by Django 5.0.6 on 2024-10-05 16:23

import django.core.validators
import users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_participant_reservations'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reservation',
            options={'verbose_name_plural': 'Reservations'},
        ),
        migrations.AlterField(
            model_name='participant',
            name='cin',
            field=models.CharField(max_length=8, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(message='This field mush contain excatly 8 digits', regex='^\\d{8}$')]),
        ),
        migrations.AlterField(
            model_name='participant',
            name='email',
            field=models.EmailField(max_length=255, unique=True, validators=[users.models.email_validator]),
        ),
    ]