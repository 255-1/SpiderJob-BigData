# Generated by Django 2.1.1 on 2020-04-07 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('big_data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='salaryWanted',
            field=models.FloatField(null=True, verbose_name='期望薪水'),
        ),
    ]
