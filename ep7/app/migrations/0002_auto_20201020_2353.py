# Generated by Django 3.0.4 on 2020-10-20 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boy',
            name='username',
            field=models.CharField(db_index=True, max_length=32),
        ),
        migrations.AlterField(
            model_name='girl',
            name='username',
            field=models.CharField(db_index=True, max_length=32),
        ),
    ]
