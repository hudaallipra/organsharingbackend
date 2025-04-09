from django import forms
from .models import Login, Doctor, User, PatientList, OrganDonation, OrganRequest

class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = ['username', 'password', 'user_type']


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['doctor_id', 'doctor_name', 'hospital', 'specialization', 'email', 'phone']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['Login_id', 'user_name', 'address', 'phone_number', 'email']


class PatientListForm(forms.ModelForm):
    class Meta:
        model = PatientList
        fields = ['patient_id', 'patient_name', 'organ_type', 'blood_group', 'hospital_name', 'gender', 'age', 'phone_number', 'email']


class OrganDonationForm(forms.ModelForm):
    class Meta:
        model = OrganDonation
        fields = ['user_id', 'organ_type', 'blood_group', 'hospital_name']


class OrganRequestForm(forms.ModelForm):
    class Meta:
        model = OrganRequest
        fields = ['patient_id', 'organ_type', 'blood_group']
