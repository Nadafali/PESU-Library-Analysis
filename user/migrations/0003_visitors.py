# Generated by Django 3.0.2 on 2020-03-09 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200205_2141'),
    ]

    operations = [
        migrations.CreateModel(
            name='visitors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('students', models.CharField(max_length=5)),
                ('staff', models.CharField(max_length=5)),
                ('visitors', models.CharField(max_length=5)),
            ],
        ),
    ]