# Generated by Django 4.1.2 on 2022-11-19 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='adherant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200, null=True)),
                ('prenom', models.CharField(max_length=200, null=True)),
                ('date_naissance', models.DateField()),
                ('telephone', models.CharField(max_length=200, null=True)),
                ('adresse', models.CharField(max_length=500, null=True)),
                ('date_enregistrement', models.DateTimeField(auto_now_add=True, null=True)),
                ('matricule', models.CharField(max_length=200, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
