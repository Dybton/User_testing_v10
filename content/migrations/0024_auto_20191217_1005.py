# Generated by Django 2.0.2 on 2019-12-17 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0023_auto_20191208_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='avg_rating',
            field=models.FloatField(null=True),
        ),
    ]