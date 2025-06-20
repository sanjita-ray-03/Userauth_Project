# Generated by Django 5.2.3 on 2025-06-15 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='address_line1',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='city',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='pincode',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='state',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[('patient', 'Patient'), ('doctor', 'Doctor')], max_length=10),
        ),
    ]
