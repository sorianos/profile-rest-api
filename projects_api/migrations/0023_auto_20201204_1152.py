# Generated by Django 2.2 on 2020-12-04 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects_api', '0022_auto_20201202_1231'),
    ]

    operations = [
        migrations.CreateModel(
            name='ElectricityConsumption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(null=True)),
                ('percentage', models.IntegerField(null=True)),
                ('annual_consumption_required_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='projects_api.AnnualConsumptionRequired')),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='projects_api.TypeEnergy')),
                ('unit_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='projects_api.Unit')),
            ],
        ),
        migrations.DeleteModel(
            name='ElectricityConsumptionData',
        ),
    ]
