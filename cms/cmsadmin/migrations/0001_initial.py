# Generated by Django 3.2.3 on 2021-06-13 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=10)),
                ('mobile', models.CharField(max_length=10)),
                ('cname', models.CharField(max_length=10)),
                ('pname', models.CharField(max_length=50)),
            ],
        ),
    ]
