# Generated by Django 3.2.4 on 2021-06-18 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instruments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50, verbose_name='Название')),
                ('anons', models.CharField(default='', max_length=250, verbose_name='Описание')),
                ('count', models.IntegerField(verbose_name='Количество на предприятии')),
            ],
        ),
    ]
