# Generated by Django 3.2.8 on 2021-12-13 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0006_alter_time_timer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_inf',
            name='national_id',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='time',
            name='timer',
            field=models.DateTimeField(null=True),
        ),
    ]
