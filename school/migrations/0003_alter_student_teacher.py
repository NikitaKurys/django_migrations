# Generated by Django 3.2.9 on 2021-12-14 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_auto_20211214_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='teacher',
            field=models.ManyToManyField(related_name='teachers', to='school.Teacher'),
        ),
    ]
