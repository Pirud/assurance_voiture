# Generated by Django 4.1.2 on 2022-11-17 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0005_client_date_enregistrement'),
    ]

    operations = [
        migrations.CreateModel(
            name='vehicule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marque', models.CharField(max_length=200, null=True)),
                ('model_v', models.CharField(max_length=200, null=True)),
                ('immatriculation', models.CharField(max_length=200, null=True)),
                ('anne_mis_circulation', models.DateField()),
                ('anne_de_fabrication', models.DateField()),
                ('type_carburant', models.CharField(choices=[('carburant', 'essence'), ('carburant', 'gazole')], max_length=200, null=True)),
                ('date_enregistrement', models.DateTimeField(auto_now_add=True, null=True)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='client.client')),
            ],
        ),
    ]
