# Generated by Django 3.2.3 on 2021-06-17 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsadmin', '0003_auto_20210614_0520'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alogin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]
