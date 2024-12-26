# Generated by Django 4.2.7 on 2024-11-07 18:31

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
            name='CreditScorePrediction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('annual_income', models.FloatField()),
                ('monthly_inhand_salary', models.FloatField()),
                ('num_bank_accounts', models.IntegerField()),
                ('num_credit_card', models.IntegerField()),
                ('interest_rate', models.FloatField()),
                ('num_credit_inquiries', models.IntegerField()),
                ('credit_history_age', models.IntegerField()),
                ('total_emi_per_month', models.FloatField()),
                ('amount_invested_monthly', models.FloatField()),
                ('predicted_credit_score', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]