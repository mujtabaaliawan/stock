# Generated by Django 4.1.4 on 2022-12-12 20:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('favourite', '0001_initial'),
        ('trader', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='favourite',
            name='trader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favourite_trader', to='trader.trader'),
        ),
        migrations.AddConstraint(
            model_name='favourite',
            constraint=models.UniqueConstraint(fields=('company', 'trader', 'monitor_field', 'is_active'), name='unique_favourite'),
        ),
    ]
