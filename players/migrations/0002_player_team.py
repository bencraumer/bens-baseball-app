# Generated by Django 2.1.4 on 2018-12-28 04:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='players.Team'),
            preserve_default=False,
        ),
    ]
