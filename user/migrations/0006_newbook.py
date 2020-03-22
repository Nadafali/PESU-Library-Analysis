# Generated by Django 3.0.2 on 2020-03-22 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20200322_2236'),
    ]

    operations = [
        migrations.CreateModel(
            name='newbook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authorname', models.CharField(max_length=300)),
                ('title', models.CharField(max_length=300)),
                ('publisher', models.CharField(max_length=300)),
                ('isbn', models.CharField(max_length=100)),
                ('edition', models.IntegerField()),
                ('price', models.IntegerField()),
                ('copies', models.IntegerField()),
                ('usertype', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='user.loginmodel')),
            ],
        ),
    ]
