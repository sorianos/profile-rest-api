# Generated by Django 2.2 on 2021-01-12 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects_api', '0038_auto_20210112_0345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='builded_surface',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='living_area',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='tier',
            field=models.IntegerField(null=True),
        ),
    ]
