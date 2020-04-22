# Generated by Django 3.0.2 on 2020-04-21 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visitorsmodel',
            name='username',
        ),
        migrations.AlterField(
            model_name='newbookmodel',
            name='username',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='register.loginmodel', to_field='username'),
        ),
        migrations.DeleteModel(
            name='bookirmodel',
        ),
        migrations.DeleteModel(
            name='loginmodel',
        ),
        migrations.DeleteModel(
            name='visitorsmodel',
        ),
    ]