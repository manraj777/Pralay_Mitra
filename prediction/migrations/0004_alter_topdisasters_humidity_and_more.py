# Generated by Django 5.0.6 on 2025-02-03 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prediction', '0003_topdisasters_windspeed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topdisasters',
            name='humidity',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='topdisasters',
            name='windSpeed',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
