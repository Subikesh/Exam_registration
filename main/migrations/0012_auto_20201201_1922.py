# Generated by Django 3.1.3 on 2020-12-01 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20201126_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Department',
            field=models.CharField(choices=[('CSE', 'CSE'), ('Mechanical', 'Mech'), ('IT', 'IT'), ('ECE', 'ECE')], max_length=35),
        ),
    ]
