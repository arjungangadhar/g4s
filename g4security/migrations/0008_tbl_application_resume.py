# Generated by Django 3.2.11 on 2022-04-25 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('g4security', '0007_tbl_employee_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_application',
            name='resume',
            field=models.CharField(default='jj', max_length=90),
            preserve_default=False,
        ),
    ]
