# Generated by Django 5.0 on 2023-12-16 02:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0008_rename_playground__first_n_e0f9a5_idx_playground__first_n_698721_idx_and_more'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='customer',
            name='playground__first_n_698721_idx',
        ),
    ]