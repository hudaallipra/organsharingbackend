from  rest_framework.serializers import ModelSerializer
from .models import *
from rest_framework import serializers

class Loginserializer(ModelSerializer):
    class Meta:
        model=Logintable
        fields=['username','password']

class Doctorserializer(ModelSerializer):
    class Meta:
        model=Doctor
        fields=['doctor_id','doctor_name','hospital','specialization','email,phone']

class Userserializer(ModelSerializer):
    class Meta:
        model=Usertable
        fields=['user_name','address','phone_number','email','image','gender','blood_group','age']


#serializers.py

class OrganDonationserializer(ModelSerializer):
    class Meta:
        model=OrganDonation
        fields=['user_id','organ_type']

class OrganRequestserializer(ModelSerializer):
    class Meta:
        model=OrganRequest
        fields=['patient_id','organ_id']

class Appointmentserializer(ModelSerializer):
    class Meta:
        model=Appointment
        fields=['patient_id','doctor_id','appointment_date','appointment_time','status']
class AppointmentSerializer1(ModelSerializer):
    doctor_name= serializers.CharField(source='doctor_id.doctor_name')
    class Meta:
        model = Appointment
        fields = ['id', 'patient_id', 'doctor_id', 'appointment_date', 'appointment_time', 'status','doctor_name','prescriptions','next_visit_date']

class AppointmentSerializer(ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id', 'patient_id', 'doctor_id', 'appointment_date', 'appointment_time', 'status']
from rest_framework import serializers
from .models import OrganDonation


class OrganDonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganDonation
        fields = '__all__'

from rest_framework import serializers
from .models import OrganRequest

class OrganRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganRequest
        fields = ['patient_id','organ_id','file']

from rest_framework import serializers

class OrganRequestSerializer1(serializers.ModelSerializer):
    organ_name = serializers.CharField(source='organ_id.organ_type.organ_name')
    organ_donor_name = serializers.CharField(source='organ_id.user_id.user_name')
    doctor_name = serializers.CharField(source='assigneddoctor.doctor_name', allow_null=True)

    class Meta:
        model = OrganRequest
        fields = '__all__'

    def get_doctor_name(self, obj):
        # If assigneddoctor or doctor_name is None, return None (null)
        if obj.assigneddoctor and obj.assigneddoctor.doctor_name:
            return obj.assigneddoctor.doctor_name
        return None
