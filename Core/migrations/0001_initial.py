# Generated by Django 4.2.4 on 2024-03-21 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=50)),
                ('Type', models.CharField(choices=[('Static Website', 'Static Website'), ('Dynamic Website', 'Dynamic Website'), ('ERP System', 'ERP System'), ('CRM System', 'CRM System'), ('Ecommerce', 'Ecommerce')], max_length=50)),
                ('Amount', models.FloatField(default=0.0)),
                ('Maintenance', models.FloatField(default=0.0)),
            ],
        ),
    ]
