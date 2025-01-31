# Generated by Django 5.1.5 on 2025-01-27 08:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patients', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('appointmentID', models.AutoField(primary_key=True, serialize=False)),
                ('date_of_visit', models.DateTimeField()),
                ('appointment_type', models.CharField(choices=[('Medical', 'Medical'), ('Eye', 'Eye')], max_length=50)),
                ('attending_doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.patient')),
            ],
        ),
    ]
