# Generated by Django 3.2.9 on 2021-12-09 06:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FinancialTracker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tracker_name', models.CharField(max_length=30)),
                ('tracker_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TrackerItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_title', models.CharField(max_length=25)),
                ('pay_amt', models.DecimalField(decimal_places=10, max_digits=19)),
                ('pay_type', models.CharField(max_length=25)),
                ('pay_description', models.CharField(max_length=100)),
                ('tracker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.financialtracker')),
            ],
        ),
    ]
