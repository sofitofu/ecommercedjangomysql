# Generated by Django 5.0 on 2023-12-16 00:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0006_rename_store_custo_first_n_a7e990_idx_customers_first_n_93c9ec_idx_and_more'),
    ]

    operations = [
        migrations.RenameIndex(
            model_name='customer',
            new_name='playground__first_n_e0f9a5_idx',
            old_name='customers_first_n_93c9ec_idx',
        ),
        migrations.AlterModelTable(
            name='customer',
            table='playground_customers',
        ),
    ]
