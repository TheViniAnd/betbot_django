# Generated by Django 2.1.3 on 2019-08-17 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='', verbose_name='Название команды:')),
            ],
            options={
                'verbose_name': 'Команда',
                'verbose_name_plural': 'Команды',
            },
        ),
    ]
