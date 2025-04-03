from django.shortcuts import render
from django.views import View

# Create your views here.




class Login(View):
    def get(Self,Request):
        return render(Request,'administrator/login.html')
    
class AddDoc(View):
    def get(Self,Request):
        return render(Request,'administrator/add doctor.html')

class ViewDoc(View):
    def get(Self,Request):
        return render(Request,'administrator/view doctor.html')
    
class ViewOrgReq(View):
    def get(Self,Request):
        return render(Request,'administrator/organ request.html')
    
class AssignDoc(View):
    def get(Self,Request):
        return render(Request,'administrator/assign doc.html')
    
class ViewOrgDon(View):
    def get(Self,Request):
        return render(Request,'administrator/view organ donation.html')

class ManageHosLoc(View):
    def get(Self,Request):
        return render(Request,'administrator/manage hospital location.html')
    
class ViewUserDet(View):
    def get(Self,Request):
        return render(Request,'administrator/view user details.html')
    
class AdminDash(View):
    def get(Self,Request):
        return render(Request,'administrator/admin dashboard.html')
    
class NewReq(View):
    def get(Self,Request):
        return render(Request,'doctor/new request.html')
    
class OrganCo(View):
    def get(Self,Request):
        return render(Request,'doctor/organ collection.html')    
    
class PatientList(View):
    def get(Self,Request):
        return render(Request,'doctor/patient list.html')

class Sched(View):
    def get(Self,Request):
        return render(Request,'doctor/schedule appointments.html')  

class DocDash(View):
    def get(Self,Request):
        return render(Request,'doctor/doctor dashboard.html')         
    
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Login
from .serializers import LoginSerializer

class LoginAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                login = Login.objects.get(pk=pk)
                serializer = LoginSerializer(login)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Login.DoesNotExist:
                return Response({'error': 'Login not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            logins = Login.objects.all()
            serializer = LoginSerializer(logins, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        try:
            login = Login.objects.get(pk=pk)
        except Login.DoesNotExist:
            return Response({'error': 'Login not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = LoginSerializer(login, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            login = Login.objects.get(pk=pk)
            login.delete()
            return Response({'message': 'Login deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Login.DoesNotExist:
            return Response({'error': 'Login not found'}, status=status.HTTP_404_NOT_FOUND)
        
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Doctor
from .serializers import DoctorSerializer

class DoctorAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                doctor = Doctor.objects.get(pk=pk)
                serializer = DoctorSerializer(doctor)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Doctor.DoesNotExist:
                return Response({'error': 'Doctor not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            doctors = Doctor.objects.all()
            serializer = DoctorSerializer(doctors, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        try:
            doctor = Doctor.objects.get(pk=pk)
        except Doctor.DoesNotExist:
            return Response({'error': 'Doctor not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = DoctorSerializer(doctor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            doctor = Doctor.objects.get(pk=pk)
            doctor.delete()
            return Response({'message': 'Doctor deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Doctor.DoesNotExist:
            return Response({'error': 'Doctor not found'}, status=status.HTTP_404_NOT_FOUND)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer

class UserAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                user = User.objects.get(pk=pk)
                serializer = UserSerializer(user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except User.DoesNotExist:
                return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
            user.delete()
            return Response({'message': 'User deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import PatientList
from .serializers import PatientListSerializer

class PatientListAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                patient = PatientList.objects.get(pk=pk)
                serializer = PatientListSerializer(patient)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except PatientList.DoesNotExist:
                return Response({'error': 'Patient not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            patients = PatientList.objects.all()
            serializer = PatientListSerializer(patients, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = PatientListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        try:
            patient = PatientList.objects.get(pk=pk)
        except PatientList.DoesNotExist:
            return Response({'error': 'Patient not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PatientListSerializer(patient, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            patient = PatientList.objects.get(pk=pk)
            patient.delete()
            return Response({'message': 'Patient deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except PatientList.DoesNotExist:
            return Response({'error': 'Patient not found'}, status=status.HTTP_404_NOT_FOUND)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import OrganDonation
from .serializers import OrganDonationSerializer

class OrganDonationAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                donation = OrganDonation.objects.get(pk=pk)
                serializer = OrganDonationSerializer(donation)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except OrganDonation.DoesNotExist:
                return Response({'error': 'Donation record not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            donations = OrganDonation.objects.all()
            serializer = OrganDonationSerializer(donations, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = OrganDonationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        try:
            donation = OrganDonation.objects.get(pk=pk)
        except OrganDonation.DoesNotExist:
            return Response({'error': 'Donation record not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = OrganDonationSerializer(donation, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            donation = OrganDonation.objects.get(pk=pk)
            donation.delete()
            return Response({'message': 'Donation record deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except OrganDonation.DoesNotExist:
            return Response({'error': 'Donation record not found'}, status=status.HTTP_404_NOT_FOUND)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import OrganRequest
from .serializers import OrganRequestSerializer

class OrganRequestAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                request_obj = OrganRequest.objects.get(pk=pk)
                serializer = OrganRequestSerializer(request_obj)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except OrganRequest.DoesNotExist:
                return Response({'error': 'Organ request not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            requests = OrganRequest.objects.all()
            serializer = OrganRequestSerializer(requests, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = OrganRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        try:
            request_obj = OrganRequest.objects.get(pk=pk)
        except OrganRequest.DoesNotExist:
            return Response({'error': 'Organ request not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = OrganRequestSerializer(request_obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            request_obj = OrganRequest.objects.get(pk=pk)
            request_obj.delete()
            return Response({'message': 'Organ request deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except OrganRequest.DoesNotExist:
            return Response({'error': 'Organ request not found'}, status=status.HTTP_404_NOT_FOUND)


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Appointment
from .serializers import AppointmentSerializer

class AppointmentAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                appointment = Appointment.objects.get(pk=pk)
                serializer = AppointmentSerializer(appointment)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Appointment.DoesNotExist:
                return Response({'error': 'Appointment not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            appointments = Appointment.objects.all()
            serializer = AppointmentSerializer(appointments, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        try:
            appointment = Appointment.objects.get(pk=pk)
        except Appointment.DoesNotExist:
            return Response({'error': 'Appointment not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = AppointmentSerializer(appointment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            appointment = Appointment.objects.get(pk=pk)
            appointment.delete()
            return Response({'message': 'Appointment deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Appointment.DoesNotExist:
            return Response({'error': 'Appointment not found'}, status=status.HTTP_404_NOT_FOUND)