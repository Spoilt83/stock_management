# Generated by Django 5.0.3 on 2024-03-15 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=50)),
                ('product_description', models.TextField()),
                ('product_quantity', models.IntegerField()),
                ('product_expiration_date', models.DateField()),
            ],
        ),
    ]
