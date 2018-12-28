# Generated by Django 2.1.4 on 2018-12-28 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('positions', models.TextField()),
                ('bats', models.TextField()),
                ('throws', models.TextField()),
                ('bio', models.TextField()),
                ('hits', models.IntegerField()),
                ('hr', models.IntegerField()),
                ('rbi', models.IntegerField()),
                ('obp', models.CharField(max_length=10)),
                ('slg', models.CharField(max_length=10)),
                ('ops', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('record', models.CharField(max_length=100)),
            ],
        ),
    ]