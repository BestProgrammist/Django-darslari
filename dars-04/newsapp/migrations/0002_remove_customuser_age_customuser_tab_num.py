# Generated by Django 4.0.4 on 2022-05-16 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='age',
        ),
        migrations.AddField(
            model_name='customuser',
            name='tab_num',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]