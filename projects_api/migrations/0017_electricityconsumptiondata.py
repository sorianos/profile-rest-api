# Generated by Django 2.2 on 2020-11-26 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects_api', '0016_annualconsumptionrequired'),
    ]

    operations = [
        migrations.CreateModel(
            name='ElectricityConsumptionData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(null=True)),
                ('type', models.CharField(max_length=255)),
                ('percentage', models.IntegerField(null=True)),
                ('annual_consumption_required_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='projects_api.AnnualConsumptionRequired')),
                ('unit_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='projects_api.Unit')),
            ],
        ),
    ]
