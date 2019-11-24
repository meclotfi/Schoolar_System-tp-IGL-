# Generated by Django 2.2.7 on 2019-11-24 22:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_number', models.CharField(max_length=50)),
                ('section', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('full_name', models.CharField(max_length=90)),
                ('matricule', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('classe', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='actors.Classe')),
            ],
        ),
    ]