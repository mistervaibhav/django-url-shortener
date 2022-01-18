# Generated by Django 4.0.1 on 2022-01-18 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shortener', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='url',
            name='uuid',
        ),
        migrations.AlterField(
            model_name='url',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='url',
            name='link',
            field=models.CharField(max_length=100),
        ),
    ]