from django.shortcuts import render
from django.views import View
from django.http.response import HttpResponse

# Create your views here.




class Loginpage(View):
    def get(self,request):
     return render(request,'administrator/login.html')
    def get(self,request):
        return render(request,'login.html')
    def post(self,request):
        username=request.POST['username']
        password=request.POST['possword']
        login_obj=LoginTable.objects.get(Username=username,Password=password)
        if login_obj.Type=="admin":
            return HttpResponse('''<script>alert("welcome to");window.loction=/viewdepartment</script>''')
    
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
    
# class PatientList(View):
#     def get(Self,Request):
#         return render(Request,'doctor/patient list.html')

class Sched(View):
    def get(Self,Request):
        return render(Request,'doctor/schedule appointments.html')  

class DocDash(View):
    def get(Self,Request):
        return render(Request,'doctor/doctor dashboard.html')         
    

    # ..........................................................api


    
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Login
from .serializers import Loginserializer, Loginserializer, PatientListserializer, Userserializer

class LoginAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                login = Login.objects.get(pk=pk)
                serializer = Loginserializer(login)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Login.DoesNotExist:
                return Response({'error': 'Login not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            logins = Login.objects.all()
            serializer = Loginserializer(logins, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = Loginserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        try:
            login = Login.objects.get(pk=pk)
        except Login.DoesNotExist:
            return Response({'error': 'Login not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = Loginserializer(login, data=request.data, partial=True)
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
from .serializers import Doctorserializer

class DoctorAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                doctor = Doctor.objects.get(pk=pk)
                serializer = Doctorserializer(doctor)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Doctor.DoesNotExist:
                return Response({'error': 'Doctor not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            doctors = Doctor.objects.all()
            serializer = Doctorserializer(doctors, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = Doctorserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        try:
            doctor = Doctor.objects.get(pk=pk)
        except Doctor.DoesNotExist:
            return Response({'error': 'Doctor not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = Doctorserializer(doctor, data=request.data, partial=True)
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
from .serializers import Userserializer

class UserAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                user = User.objects.get(pk=pk)
                serializer = Userserializer(user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except User.DoesNotExist:
                return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            users = User.objects.all()
            serializer = Userserializer(users, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = Userserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = Userserializer(user, data=request.data, partial=True)
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
from .serializers import PatientListserializer

class PatientListAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                patient = PatientList.objects.get(pk=pk)
                serializer = PatientListserializer(patient)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except PatientList.DoesNotExist:
                return Response({'error': 'Patient not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            patients = PatientList.objects.all()
            serializer = PatientListserializer(patients, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = PatientListserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        try:
            patient = PatientList.objects.get(pk=pk)
        except PatientList.DoesNotExist:
            return Response({'error': 'Patient not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PatientListserializer(patient, data=request.data, partial=True)
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
from .serializers import OrganDonationserializer

class OrganDonationAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                donation = OrganDonation.objects.get(pk=pk)
                serializer = OrganDonationserializer(donation)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except OrganDonation.DoesNotExist:
                return Response({'error': 'Donation record not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            donations = OrganDonation.objects.all()
            serializer = OrganDonationserializer(donations, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = OrganDonationserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        try:
            donation = OrganDonation.objects.get(pk=pk)
        except OrganDonation.DoesNotExist:
            return Response({'error': 'Donation record not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = OrganDonationserializer(donation, data=request.data, partial=True)
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
from .serializers import OrganRequestserializer

class OrganRequestAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                request_obj = OrganRequest.objects.get(pk=pk)
                serializer = OrganRequestserializer(request_obj)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except OrganRequest.DoesNotExist:
                return Response({'error': 'Organ request not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            requests = OrganRequest.objects.all()
            serializer = OrganRequestserializer(requests, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = OrganRequestserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        try:
            request_obj = OrganRequest.objects.get(pk=pk)
        except OrganRequest.DoesNotExist:
            return Response({'error': 'Organ request not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = OrganRequestserializer(request_obj, data=request.data, partial=True)
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
from .serializers import Appointmentserializer

class AppointmentAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                appointment = Appointment.objects.get(pk=pk)
                serializer = Appointmentserializer(appointment)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Appointment.DoesNotExist:
                return Response({'error': 'Appointment not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            appointments = Appointment.objects.all()
            serializer = Appointmentserializer(appointments, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = Appointmentserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        try:
            appointment = Appointment.objects.get(pk=pk)
        except Appointment.DoesNotExist:
            return Response({'error': 'Appointment not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = Appointmentserializer(appointment, data=request.data, partial=True)
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
        
from rest_framework.views import APIView

class DonorRegistrationApi(APIView):
    print("*****")
    def post(self, request):
        print("###############",request.data)
        user_serial =  Userserializer(data=request.data)
        login_serial = Loginserializer(data=request.data)
        data_valid = user_serial.is_valid()
        login_valid = login_serial.is_valid()
        print("---dta------>", data_valid)
        print("---login------>", login_valid)
        if data_valid and login_valid:
            print("------------>")
            login_profile = login_serial.save(user_type='donar')
            user_serial.save(login_page=login_profile)
            return Response(user_serial.data, status=status.HTTP_201_CREATED)
        return Response({'login_error': login_serial.errors if not login_valid else None,
                         'user_error': user_serial.errors if not data_valid else None}, status=status.HTTP_400_BAD_REQUEST)


from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_200_OK


class LoginPageApi(APIView):
    def post(self, request):
        response_dict= {}
        password = request.data.get("password")
        print("Password ------------------> ",password)
        username = request.data.get("username")
        print("Username ------------------> ",username)
        try:
            user = Login.objects.filter(username=username, password=password).first()
            print("user_obj :-----------", user)
        except Login.DoesNotExist:
            response_dict["message"] = "No account found for this username. Please signup."
            return Response(response_dict, HTTP_200_OK)
      
        if user.Type == "donor":
            response_dict = {
                "login_id": str(user.id),
                "user_type": user.Type,
                "status": "success",
            }   
            print("User details :--------------> ",response_dict)
            return Response(response_dict, HTTP_200_OK)
        else:
            response_dict["message "] = "Your account has not been approved yet or you are a CLIENT user."
            return Response(response_dict, HTTP_200_OK)