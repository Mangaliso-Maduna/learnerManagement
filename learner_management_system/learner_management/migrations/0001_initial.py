# Generated by Django 4.1.7 on 2023-04-01 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='personal_Information',
            fields=[
                ('id_passport_no', models.CharField(max_length=13, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=225)),
                ('last_name', models.CharField(max_length=225)),
                ('email_address', models.CharField(max_length=225)),
                ('contact_num', models.CharField(max_length=225)),
                ('title', models.CharField(max_length=225)),
                ('date_of_birth', models.DateField()),
                ('race', models.CharField(max_length=225)),
                ('gender', models.CharField(max_length=225)),
                ('citizenship', models.CharField(max_length=225)),
                ('disability', models.CharField(max_length=225)),
                ('profile_pic', models.FileField(upload_to='')),
                ('personal_summary', models.CharField(max_length=550)),
                ('employment_status', models.CharField(max_length=550)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=225)),
                ('usertype', models.CharField(max_length=225)),
                ('password', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='placement',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=225)),
                ('industry', models.CharField(max_length=225)),
                ('personal_information_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learner_management.personal_information')),
            ],
        ),
        migrations.AddField(
            model_name='personal_information',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learner_management.users'),
        ),
        migrations.CreateModel(
            name='experience',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=225)),
                ('industry', models.CharField(max_length=225)),
                ('company', models.CharField(max_length=225)),
                ('occupation', models.CharField(max_length=225)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('reason_for_leaving', models.CharField(max_length=225)),
                ('duties_description', models.CharField(max_length=225)),
                ('personal_information_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learner_management.personal_information')),
            ],
        ),
        migrations.CreateModel(
            name='education',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('learning_institute', models.CharField(max_length=225)),
                ('qualification', models.CharField(max_length=225)),
                ('qualification_type', models.CharField(max_length=225)),
                ('achievement_status', models.CharField(max_length=225)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('field_of_study', models.CharField(max_length=225)),
                ('graduation_date', models.DateField()),
                ('student_number', models.CharField(max_length=225)),
                ('personal_information_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learner_management.personal_information')),
            ],
        ),
        migrations.CreateModel(
            name='certificates',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('body_institute', models.CharField(max_length=225)),
                ('professional_registration', models.CharField(max_length=225)),
                ('qualification_type', models.CharField(max_length=225)),
                ('achievement_status', models.CharField(max_length=225)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('graduation_date', models.DateField()),
                ('personal_information_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learner_management.personal_information')),
            ],
        ),
        migrations.CreateModel(
            name='address',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('street', models.CharField(max_length=225)),
                ('city', models.CharField(max_length=225)),
                ('state', models.CharField(max_length=225)),
                ('postal_code', models.CharField(max_length=225)),
                ('personal_information_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learner_management.personal_information')),
            ],
        ),
    ]