# Generated by Django 4.1.2 on 2022-10-27 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_puzzles_puzzle'),
    ]

    operations = [
        migrations.AddField(
            model_name='puzzle',
            name='size',
            field=models.IntegerField(default=9),
            preserve_default=False,
        ),
    ]
