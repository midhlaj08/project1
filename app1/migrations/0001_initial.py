# Generated by Django 4.2.2 on 2023-07-27 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='table_cake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('photo', models.CharField(max_length=500)),
                ('address', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'table_cake',
            },
        ),
    ]
