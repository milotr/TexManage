# Generated by Django 4.0.2 on 2022-03-05 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_alter_customer_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='length',
            field=models.FloatField(default=100),
            preserve_default=False,
        ),
    ]
