# Generated by Django 3.1.1 on 2020-09-10 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SatispayPayment',
            fields=[
                ('payment_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('code_identifier', models.CharField(max_length=255)),
                ('payment_type', models.CharField(max_length=255)),
                ('amount_unit', models.IntegerField()),
                ('currency', models.CharField(max_length=3)),
                ('status', models.CharField(max_length=255)),
                ('expired', models.BooleanField()),
                ('metadata', models.TextField(blank=True, null=True)),
                ('sender_id', models.CharField(blank=True, max_length=255, null=True)),
                ('sender_type', models.CharField(max_length=255)),
                ('sender_name', models.CharField(blank=True, max_length=255, null=True)),
                ('receiver_id', models.CharField(max_length=255)),
                ('receiver_type', models.CharField(max_length=255)),
                ('insert_date', models.DateTimeField()),
                ('expire_date', models.DateTimeField()),
                ('external_code', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
