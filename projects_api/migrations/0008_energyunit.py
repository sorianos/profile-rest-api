# Generated by Django 2.2 on 2020-11-11 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects_api', '0007_volumeunit'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnergyUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_energy_unit', models.CharField(max_length=255)),
            ],
        ),
    ]
