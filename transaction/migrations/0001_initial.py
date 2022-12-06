# Generated by Django 4.1.2 on 2022-12-06 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nature', models.CharField(max_length=10)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('mode', models.CharField(max_length=255)),
                ('volume', models.FloatField()),
                ('current_price', models.FloatField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction_category', to='category.category')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction_company', to='company.company')),
            ],
        ),
    ]
