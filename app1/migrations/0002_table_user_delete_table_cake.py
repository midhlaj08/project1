# Generated by Django 4.2.2 on 2023-07-28 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='table_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('photo', models.CharField(max_length=500)),
                ('address', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'table_user',
            },
        ),
        migrations.DeleteModel(
            name='table_cake',
        ),
    ]
