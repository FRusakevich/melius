# Generated by Django 3.1 on 2020-09-16 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tovar',
            name='proizvoditel',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='rel_proizdodotel', to='test_app.proizvoditel'),
        ),
    ]
