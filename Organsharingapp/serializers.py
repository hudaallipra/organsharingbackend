from  rest_framework.serializers import ModelSerializer
from .models import *

class Loginserializer(ModelSerializer):
    class Meta:
        model=Logintable
        fields=['username','password','user_type']

class Doctorserializer(ModelSerializer):
    class Meta:
        model=Doctor
        fields=['doctor_id','doctor_name','hospital','specialization','email,phone']

class Userserializer(ModelSerializer):
    class Meta:
        model=Usertable
        fields=['Login_id','user_name','address','phone_number','email']


class OrganDonationserializer(ModelSerializer):
    class Meta:
        model=OrganDonation
        fields=['user_id','organ_type','blood_group','hospital_name']

class OrganRequestserializer(ModelSerializer):
    class Meta:
        model=OrganRequest
        fields=['patient_id','organ_type','blood_group','hospital_name']

class Appointmentserializer(ModelSerializer):
    class Meta:
        model=Appointment
        fields=['patient_id','doctor_id','date','time','status']