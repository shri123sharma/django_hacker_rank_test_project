# Generated by Django 4.2.5 on 2023-09-18 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing_model_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mymodel',
            name='number',
            field=models.IntegerField(default=0),
        ),
    ]