from django.db import models

# Create your models here.
class Login(models.Model):
    username=models.CharField(max_length=100,null=True,blank=True)
    password=models.CharField(max_length=100,null=True,blank=True)
    user_type=models.CharField(max_length=100,null=True,blank=True)

class Doctor(models.Model):
    doctor_id=models.ForeignKey(Login,on_delete=models.CASCADE,null=True,blank=True)
    doctor_name=models.CharField(max_length=100,null=True,blank=True)
    hospital=models.CharField(max_length=100,null=True,blank=True)
    specialization=models.CharField(max_length=100,null=True,blank=True)
    email=models.CharField(max_length=100,null=True,blank=True)
    phone=models.CharField(max_length=100,null=True,blank=True)

class User(models.Model):
    Login_id=models.ForeignKey(Login,on_delete=models.CASCADE,null=True,blank=True)
    user_name=models.CharField(max_length=100,null=True,blank=True)
    address=models.CharField(max_length=100,null=True,blank=True)
    phone_number=models.CharField(max_length=100,null=True,blank=True)
    email=models.CharField(max_length=100,null=True,blank=True)

class PatientList(models.Model):
    patient_id=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    patient_name=models.CharField(max_length=100,null=True,blank=True)
    organ_type=models.CharField(max_length=100,null=True,blank=True)
    blood_group=models.CharField(max_length=100,null=True,blank=True)
    hospital_name=models.CharField(max_length=100,null=True,blank=True)
    gender=models.CharField(max_length=100,null=True,blank=True)
    age=models.CharField(max_length=100,null=True,blank=True)
    phone_number=models.CharField(max_length=100,null=True,blank=True)
    email=models.CharField(max_length=100,null=True,blank=True)



class OrganDonation(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    organ_type=models.CharField(max_length=100,null=True,blank=True)
    blood_group=models.CharField(max_length=100,null=True,blank=True)
    hospital_name=models.CharField(max_length=100,null=True,blank=True)

class OrganRequest(models.Model):
    patient_id=models.ForeignKey(PatientList,on_delete=models.CASCADE,null=True,blank=True)
    organ_type=models.CharField(max_length=100,null=True,blank=True)
    blood_group=models.CharField(max_length=100,null=True,blank=True)
    hospital_name=models.CharField(max_length=100,null=True,blank=True)


class Appointment(models.Model):
    patient_id=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    doctor_id=models.ForeignKey(Doctor,on_delete=models.CASCADE,null=True,blank=True)
    date=models.CharField(max_length=100,null=True,blank=True)
    time=models.CharField(max_length=100,null=True,blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)

