# Generated by Django 3.0.6 on 2020-05-29 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invmgsys', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='partsinproduct',
            name='qty',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='storagelocation',
            name='qty',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
