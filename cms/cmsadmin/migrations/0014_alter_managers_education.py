# Generated by Django 3.2.3 on 2021-06-21 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsadmin', '0013_auto_20210621_0451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='managers',
            name='education',
            field=models.CharField(max_length=50),
        ),
    ]
