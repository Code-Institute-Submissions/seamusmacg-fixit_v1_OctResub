# Generated by Django 3.2.6 on 2021-09-08 19:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('default_phone', models.CharField(max_length=18)),
                ('default_postcode', models.CharField(blank=True, max_length=15, null=True)),
                ('default_town', models.CharField(max_length=50)),
                ('default_address', models.CharField(max_length=100)),
                ('default_country', django_countries.fields.CountryField(blank=True, max_length=2)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
