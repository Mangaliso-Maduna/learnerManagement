# Generated by Django 4.1.7 on 2023-04-13 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learner_management', '0003_rename_citizenship_personal_information_profession_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personal_information',
            name='profile_pic',
        ),
    ]
