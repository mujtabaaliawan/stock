# Generated by Django 4.1.3 on 2022-12-01 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('favourite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(default='trader', max_length=10)),
                ('mobile_number', models.CharField(default='0', max_length=20)),
                ('favourite', models.ManyToManyField(blank=True, to='favourite.favourite')),
            ],
        ),
    ]
