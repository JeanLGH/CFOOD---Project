# Generated by Django 3.2.5 on 2022-04-24 00:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cfood', '0004_ingredients'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredients',
            old_name='ingredient',
            new_name='ingredients',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]