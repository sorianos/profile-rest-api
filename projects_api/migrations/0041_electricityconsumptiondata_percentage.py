# Generated by Django 2.2 on 2021-01-21 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects_api', '0040_auto_20210121_0833'),
    ]

    operations = [
        migrations.AddField(
            model_name='electricityconsumptiondata',
            name='percentage',
            field=models.IntegerField(null=True),
        ),
    ]
