# Generated by Django 3.0.4 on 2020-10-06 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_userinfo_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usergroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
            ],
        ),
    ]
