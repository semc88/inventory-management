# Generated by Django 3.0.6 on 2020-05-29 22:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invmgsys', '0003_auto_20200529_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storagelocation',
            name='part_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='invmgsys.Part'),
        ),
    ]