# Generated by Django 3.0.4 on 2020-10-21 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=32)),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=64)),
                ('gender', models.IntegerField(choices=[(1, 'boy'), (2, 'girl')])),
            ],
        ),
        migrations.CreateModel(
            name='btoy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='b', to='app01.UserInfo')),
                ('g', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='a', to='app01.UserInfo')),
            ],
        ),
    ]