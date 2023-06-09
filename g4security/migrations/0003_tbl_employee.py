# Generated by Django 3.2.6 on 2022-01-07 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('g4security', '0002_tbl_selection_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(max_length=90)),
                ('job_id', models.CharField(max_length=90)),
                ('name', models.CharField(max_length=90)),
                ('address', models.CharField(max_length=90)),
                ('phone', models.CharField(max_length=90)),
                ('email', models.CharField(max_length=90)),
                ('date_of_birth', models.CharField(max_length=90)),
                ('age', models.CharField(max_length=90)),
                ('gender', models.CharField(max_length=90)),
                ('qualification', models.CharField(max_length=90)),
                ('experience', models.CharField(max_length=90)),
                ('remark', models.CharField(max_length=90)),
                ('date_of_join', models.CharField(max_length=90)),
            ],
            options={
                'db_table': 'tbl_employee',
            },
        ),
    ]
