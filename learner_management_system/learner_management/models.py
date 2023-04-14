from django.db import models

# Create your models here.
class Users(models.Model):
    id=models.AutoField(primary_key=True)
    username = models.CharField(max_length=225)
    email = models.CharField(max_length=225)
    password = models.CharField(max_length=225)

class personal_Information(models.Model):
    id_passport_no = models.CharField(max_length=13, primary_key=True)
    user_id = models.ForeignKey(Users,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    email_address = models.CharField(max_length=225)
    contact_num = models.CharField(max_length=225)
    profession = models.CharField(max_length=225)
    date_of_birth = models.DateField()
    #profile_pic=models.FileField()
    personal_summary = models.CharField(max_length=550)
    # race = models.CharField(max_length=225)
    # gender = models.CharField(max_length=225)
    # citizenship = models.CharField(max_length=225)
    # disability = models.CharField(max_length=225)
    # employment_status = models.CharField(max_length=550)

class education(models.Model):
    id=models.AutoField(primary_key=True)
    personal_information_id = models.ForeignKey(personal_Information,on_delete=models.CASCADE)
    learning_institute = models.CharField(max_length=225)
    qualification = models.CharField(max_length=225)
    qualification_type = models.CharField(max_length=225)
    achievement_status = models.CharField(max_length=225)
    start_date = models.DateField()
    end_date = models.DateField()
    field_of_study = models.CharField(max_length=225)
    graduation_date = models.DateField()
    student_number = models.CharField(max_length=225)

class experience(models.Model):
    id=models.AutoField(primary_key=True)
    personal_information_id = models.ForeignKey(personal_Information,on_delete=models.CASCADE)
    name = models.CharField(max_length=225)
    industry = models.CharField(max_length=225)
    company = models.CharField(max_length=225)
    occupation = models.CharField(max_length=225)
    start_date = models.DateField()
    end_date = models.DateField()
    reason_for_leaving = models.CharField(max_length=225)
    duties_description = models.CharField(max_length=225)

class certificates(models.Model):
    id=models.AutoField(primary_key=True)
    personal_information_id = models.ForeignKey(personal_Information,on_delete=models.CASCADE)
    body_institute = models.CharField(max_length=225)
    professional_registration = models.CharField(max_length=225)
    qualification_type = models.CharField(max_length=225)
    achievement_status = models.CharField(max_length=225)
    start_date = models.DateField()
    end_date = models.DateField()
    graduation_date = models.DateField()

class address(models.Model):
    id=models.AutoField(primary_key=True)
    personal_information_id = models.ForeignKey(personal_Information,on_delete=models.CASCADE)
    street = models.CharField(max_length=225)
    city = models.CharField(max_length=225)
    state = models.CharField(max_length=225)
    postal_code = models.CharField(max_length=225)

class placement(models.Model):
    id=models.AutoField(primary_key=True)
    personal_information_id = models.ForeignKey(personal_Information,on_delete=models.CASCADE)
    name = models.CharField(max_length=225)
    industry = models.CharField(max_length=225)
