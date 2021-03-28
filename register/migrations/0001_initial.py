# Generated by Django 3.0.4 on 2021-03-26 22:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('org_id', models.IntegerField(auto_created=True, blank=True, primary_key=True, serialize=False)),
                ('orgname', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(max_length=30, unique=True)),
                ('phone', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.IntegerField(auto_created=True, blank=True, primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(max_length=30, unique=True)),
                ('phone', models.IntegerField(unique=True)),
                ('org_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='register.Organization')),
            ],
        ),
    ]
