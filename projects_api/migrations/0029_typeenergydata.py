# Generated by Django 2.2 on 2020-12-07 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects_api', '0028_auto_20201207_0042'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeEnergyData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=35, max_digits=45, null=True)),
                ('potential_type_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='projects_api.PotentialType')),
                ('type_energy_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='projects_api.TypeEnergy')),
                ('unit_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='projects_api.Unit')),
            ],
        ),
    ]
