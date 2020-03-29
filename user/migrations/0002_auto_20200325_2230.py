# Generated by Django 3.0.2 on 2020-03-25 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookirmodel',
            name='bookissue',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='bookirmodel',
            name='bookrenew',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='bookirmodel',
            name='bookreturn',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='newbookmodel',
            name='copies',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='newbookmodel',
            name='edition',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='newbookmodel',
            name='price',
            field=models.PositiveIntegerField(default=0),
        ),
    ]