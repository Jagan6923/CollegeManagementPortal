# Generated by Django 5.0.1 on 2024-01-13 06:51

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = [
        ('EmployeeApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Feedbackmailid', models.CharField(max_length=100)),
                ('Feedback', models.CharField(max_length=100)),
            ],
        ),
    ]
