# Generated by Django 4.1.7 on 2023-03-14 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('emp_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('emp_name', models.TextField()),
                ('emp_category', models.TextField()),
                ('rm_id', models.IntegerField(unique=True)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
        migrations.CreateModel(
            name='RmRequested',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trn_name', models.TextField()),
                ('urgency', models.IntegerField()),
                ('emp_id', models.IntegerField()),
                ('tm_acceptance', models.TextField()),
                ('rej_reason', models.TextField()),
                ('session_date', models.TextField()),
                ('session_time', models.TextField()),
            ],
            options={
                'db_table': 'rm_requested',
            },
        ),
    ]
