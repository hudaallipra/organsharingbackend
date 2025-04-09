from django import forms
from .models import Logintable, Doctor, Usertable, OrganDonation, OrganRequest

class LoginForm(forms.ModelForm):
    class Meta:
        model = Logintable
        fields = ['username', 'password', 'user_type']


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['doctor_id', 'doctor_name', 'hospital', 'specialization', 'email', 'phone']


class UserForm(forms.ModelForm):
    class Meta:
        model = Usertable
        fields = ['Login_id', 'user_name', 'address', 'phone_number', 'email']

class OrganDonationForm(forms.ModelForm):
    class Meta:
        model = OrganDonation
        fields = ['user_id', 'organ_type']


class OrganRequestForm(forms.ModelForm):
    class Meta:
        model = OrganRequest
        fields = ['patient_id', 'organ_id',]
