# Generated by Django 5.1.5 on 2025-02-01 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserWaterIntake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercises_type', models.CharField(choices=[('cardio', 'Cardio'), ('weights', 'Weights'), ('none', 'None')], max_length=50)),
                ('water_amount', models.FloatField()),
                ('timestap', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
