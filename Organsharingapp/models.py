from django.db import models

# Create your models here.
class Logintable(models.Model):
    username=models.CharField(max_length=100,null=True,blank=True)
    password=models.CharField(max_length=100,null=True,blank=True)
    user_type=models.CharField(max_length=100,null=True,blank=True)
class Organ(models.Model):
    organ_name=models.CharField(max_length=100,null=True,blank=True)


class Doctor(models.Model):
    doctor_id=models.ForeignKey(Logintable,on_delete=models.CASCADE,null=True,blank=True)
    doctor_name=models.CharField(max_length=100,null=True,blank=True)
    hospital=models.CharField(max_length=100,null=True,blank=True)
    specialization=models.ForeignKey(Organ,on_delete=models.CASCADE,null=True,blank=True)
    email=models.CharField(max_length=100,null=True,blank=True)
    phone=models.CharField(max_length=100,null=True,blank=True)

class Usertable(models.Model):
    Login_id=models.ForeignKey(Logintable,on_delete=models.CASCADE,null=True,blank=True)
    user_name=models.CharField(max_length=100,null=True,blank=True)
    address=models.CharField(max_length=100,null=True,blank=True)
    image=models.FileField(upload_to='profileimage',null=True,blank=True)
    phone_number=models.CharField(max_length=100,null=True,blank=True)
    email=models.CharField(max_length=100,null=True,blank=True)
    blood_group=models.CharField(max_length=100,null=True,blank=True)
    gender=models.CharField(max_length=100,null=True,blank=True)
    age=models.CharField(max_length=100,null=True,blank=True)


class OrganDonation(models.Model):
    user_id=models.ForeignKey(Usertable,on_delete=models.CASCADE,null=True,blank=True)
    organ_type=models.ForeignKey(Organ,on_delete=models.CASCADE,null=True,blank=True)
    file=models.FileField(upload_to='organdonation',null=True,blank=True)

class OrganRequest(models.Model):
    patient_id=models.ForeignKey(Usertable,on_delete=models.CASCADE,null=True,blank=True)
    organ_id=models.ForeignKey(OrganDonation,on_delete=models.CASCADE,null=True,blank=True)
    assigneddoctor=models.ForeignKey(Doctor,on_delete=models.CASCADE,null=True,blank=True)
    file=models.FileField(upload_to='organrequest',null=True,blank=True)
    status=models.CharField(max_length=100,null=True,blank=True,default='pending')
    created_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)


class Appointment(models.Model):
    patient_id=models.ForeignKey(Usertable,on_delete=models.CASCADE,null=True,blank=True)
    doctor_id=models.ForeignKey(Doctor,on_delete=models.CASCADE,null=True,blank=True)
    appointment_date=models.CharField(max_length=100,null=True,blank=True)
    appointment_time=models.CharField(max_length=100,null=True,blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)
    next_visit_date=models.CharField(max_length=100,null=True,blank=True)
    prescriptions=models.CharField(max_length=400,null=True,blank=True)