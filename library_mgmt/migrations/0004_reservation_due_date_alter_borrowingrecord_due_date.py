# Generated by Django 5.1.6 on 2025-02-18 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_mgmt', '0003_alter_borrowingrecord_due_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='due_date',
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name='borrowingrecord',
            name='due_date',
            field=models.DateField(default=None),
        ),
    ]
