from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.http.response import HttpResponse
from .forms import *

# Create your views here.




class Loginpage(View):
    def get(self,request):
     return render(request,'administrator/login.html')
    def post(self,request):
        username=request.POST['username']
        password=request.POST['password']
        print(username,password)
        try:
            print("hhhhh")
            login_obj=Logintable.objects.get(username=username,password=password)
            print(login_obj)
            request.session['userid']=login_obj.id
            if login_obj.user_type=="admin":
                print("gggg")
                return render(request,'administrator/admindashboard.html')
               
            elif login_obj.user_type=="doctor":
                return redirect('doctor dashboard')
                
        except Logintable.DoesNotExist:
            return HttpResponse('''<script>alert("invalid username or password");window.location=/</script>''')
class AddDoc(View):
    def get(Self,Request):
        return render(Request,'administrator/add doctor.html')
    def post(self,request):
        form=DoctorForm(request.POST)
        if form.is_valid():
            user=Logintable.objects.create(username=request.POST['email'],password=request.POST['password'],user_type='doctor')
            doc=form.save(commit=False)
            doc.doctor_id=user
            doc.save()
            
        return HttpResponse('''<script>alert("Doctor added successfully");window.location='/viewdoctor';</script>''')

class DeleteDoc(View):
    def get(Self,Request,id):
        doc=Doctor.objects.get(id=id)
        doc.delete()
        return HttpResponse('''<script>alert("Doctor deleted successfully");window.location='/viewdoctor';</script>''')
    
  
class EditDoc(View):
    def get(Self,Request,id):
        doc=Doctor.objects.get(id=id)
        return render(Request,'administrator/editdoctor.html',{'doc':doc})
    def post(self, request, id):
        # Fetch the doctor and their associated login record
        doc = Doctor.objects.get(id=id)
        login_info = Logintable.objects.get(id=doc.doctor_id.id)  # Assuming 'doctor_id' links to the Login table
        
        # Create a form with the doctor data from the request
        form = DoctorForm(request.POST, instance=doc)
        
        if form.is_valid():
            # Update the login details (username and password)
            login_info.username = request.POST['email']
            login_info.password = request.POST['password']
            login_info.save()  # Save the updated login information
            
            # Save the doctor form, but don't commit yet
            updated_doc = form.save(commit=False)
            updated_doc.doctor_id = login_info  # Link the updated login_info back to the doctor
            updated_doc.save()  # Save the doctor details
            
            # Redirect after saving, or return a success message
            return HttpResponse('''<script>alert("Doctor details updated successfully!");window.location='/viewdoctor';</script>''')
        else:
            # Handle the case where the form is not valid
            return render(request, 'administrator/editdoctor.html', {'doc': doc, 'login_info': login_info, 'form': form})
class ViewDoc(View):
    def get(Self,Request):
        doc=Doctor.objects.all()
        return render(Request,'administrator/view doctor.html',{'doc':doc})

    
class ViewOrgReq(View):
    def get(Self,Request):
        orgreq=OrganRequest.objects.all()
        doc=Doctor.objects.all()
        return render(Request,'administrator/organrequest.html',{'org':orgreq,'doc':doc})
        

class organrequestupdate(View):
    def post(self, request, id):
        orgreq = get_object_or_404(OrganRequest, id=id)
        doctor_id = request.POST.get('assigneddoctor')
        if doctor_id:
            doctor = get_object_or_404(Doctor, id=doctor_id)
            orgreq.assigneddoctor = doctor
            orgreq.save()
            return redirect('organ request')

class AssignDoc(View):
    def get(Self,Request):
        return render(Request,'administrator/assign doc.html')
    
class ViewOrgDon(View):
    def get(Self,Request):
        orgdon=OrganDonation.objects.all()
        print(orgdon)
        return render(Request,'administrator/vieworgandonation.html',{'orgdon':orgdon})
        

class ManageHosLoc(View):
    def get(Self,Request):
        return render(Request,'administrator/manage hospital location.html')
    
class ViewUserDet(View):
    def get(Self,Request):
        userdet=Usertable.objects.all()
        return render(Request,'administrator/view user details.html',{'userdet':userdet})
class PatientList(View):
    def get(Self,Request):
        userdet=Usertable.objects.all()
        return render(Request,'doctor/patient list.html',{'userdet':userdet})

    
class AdminDash(View):
    def get(Self,Request):
        return render(Request,'administrator/admindashboard.html')
    
class NewReq(View):
    def get(Self,Request):
        orgreq=OrganRequest.objects.all()
        return render(Request,'doctor/new request.html',{'orgreq':orgreq})
    
class OrganCo(View):
    def get(Self,Request):
        orgdon=OrganDonation.objects.all()
        return render(Request,'doctor/organ collection.html', {'orgdon':orgdon})    
    
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
from .models import Logintable
from .serializers import Loginserializer, Loginserializer, OrganRequestSerializer1, Userserializer

class LoginAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                login = Logintable.objects.get(pk=pk)
                serializer = Loginserializer(login)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Logintable.DoesNotExist:
                return Response({'error': 'Login not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            logins = Logintable.objects.all()
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
            login = Logintable.objects.get(pk=pk)
        except Logintable.DoesNotExist:
            return Response({'error': 'Login not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = Loginserializer(login, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            login = Logintable.objects.get(pk=pk)
            login.delete()
            return Response({'message': 'Login deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Logintable.DoesNotExist:
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
from .models import Usertable
from .serializers import Userserializer

class UserAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                user = Usertable.objects.get(Login_id__pk=pk)
                serializer = Userserializer(user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Usertable.DoesNotExist:
                return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            users = Usertable.objects.all()
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
            user = Usertable.objects.get(pk=pk)
        except Usertable.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = Userserializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            user = Usertable.objects.get(pk=pk)
            user.delete()
            return Response({'message': 'User deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Usertable.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

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
#views.py
        
from rest_framework.views import APIView

class DonorRegistrationApi(APIView):
    print("*")
    def post(self, request):
        print("###############",request.data)
        data={}
        data=request.data
        data['username']=request.data.get('email')
        print(data)

        user_serial =  Userserializer(data=request.data)
        login_serial = Loginserializer(data=data)
        data_valid = user_serial.is_valid()
        login_valid = login_serial.is_valid()
        print("---dta------>", data_valid)
        print("---login------>", login_valid)
        if data_valid and login_valid:
            print("------------>")
            login_profile = login_serial.save(user_type='donor')
            user_serial.save(Login_id=login_profile)
            return Response(user_serial.data, status=status.HTTP_201_CREATED)
        return Response({'login_error': login_serial.errors if not login_valid else None,
                         'user_error': user_serial.errors if not data_valid else None}, status=status.HTTP_400_BAD_REQUEST)


from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_200_OK


class LoginPageApi(APIView):
    def post(self, request):
        print(request.data)
        response_dict= {}
        password = request.data.get("password")
        print("Password ------------------> ",password)
        username = request.data.get("username")
        print("Username ------------------> ",username)
        try:
            user = Logintable.objects.filter(username=username, password=password).first()
            print("user_obj :-----------", user)
        except Logintable.DoesNotExist:
            response_dict["message"] = "No account found for this username. Please signup."
            return Response(response_dict, HTTP_200_OK)
      
        if user.user_type == "donor":
            response_dict = {
                "login_id": str(user.id),
                "user_type": user.user_type,
                "status": "success",
            }   
            print("User details :--------------> ",response_dict)
            return Response(response_dict, HTTP_200_OK)
        else:
            response_dict["message "] = "Your account has not been approved yet or you are a CLIENT user."
            return Response(response_dict, HTTP_200_OK)
        
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Organ, OrganDonation
 # create this for user details

class organ_donor_list(APIView):
    def get(self,request):
        data = []

        organs = Organ.objects.all()

        for organ in organs:
            donations = OrganDonation.objects.filter(organ_type=organ)
            print(donations)

            donors = []
            for donation in donations:
                user = donation.user_id
                # print(user)
                donors.append({
                    'donation_id': donation.id,
                    'id': user.id,
                    "user_name": user.user_name,
                    "age": user.age,
                    "email": user.email,
                    "phone_number": user.phone_number,
                    "profile_image":request.build_absolute_uri(user.image.url) if user.image else None,
                    "address":user.address,
                    "gender":user.gender,
                    "bloodgroup":user.blood_group,


                    
                    # add other user fields as required
                })

            data.append({
                "category": organ.organ_name,
                "categoryid":organ.id,
                "donors": donors
            })
            print(data)

        return Response(data)
    
# class vieworgans(APIView):
#     def get(self,request):

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import OrganDonation
from .serializers import OrganDonationSerializer


class OrganDonationAPI(APIView):

    def get(self, request):
        donations = OrganDonation.objects.all()
        serializer = OrganDonationSerializer(donations, many=True)
        return Response(serializer.data)

    def post(self, request):
        print(request.data)
        data={}
        data=request.data
        data['user_id']=Usertable.objects.get(Login_id__id=request.data.get('user_id')).id

        serializer = OrganDonationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            donation = OrganDonation.objects.get(pk=pk)
        except OrganDonation.DoesNotExist:
            return Response({'error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = OrganDonationSerializer(donation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            donation = OrganDonation.objects.get(pk=pk)
        except OrganDonation.DoesNotExist:
            return Response({'error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)

        donation.delete()
        return Response({'message': 'Deleted Successfully'}, status=status.HTTP_204_NO_CONTENT)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import OrganRequest
from .serializers import OrganRequestSerializer


class OrganRequestAPIView(APIView):

    def get(self, request, id=None):
        if id is None:
            organ_requests = OrganRequest.objects.all()
        else:
            organ_requests = OrganRequest.objects.filter(patient_id__Login_id__id=id)

        serializer = OrganRequestSerializer1(organ_requests, many=True)
        print(serializer.data)
        return Response(serializer.data)

    def post(self, request):
        print(request.data)
        data={}
        data=request.data
        data['patient_id']=Usertable.objects.get(Login_id__id=request.data.get('patient_id')).id

        serializer = OrganRequestSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            organ_request = OrganRequest.objects.get(id=pk)
        except OrganRequest.DoesNotExist:
            return Response({"error": "Not Found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = OrganRequestSerializer(organ_request, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            organ_request = OrganRequest.objects.get(id=pk)
        except OrganRequest.DoesNotExist:
            return Response({"error": "Not Found"}, status=status.HTTP_404_NOT_FOUND)

        organ_request.delete()
        return Response({"message": "Deleted Successfully"}, status=status.HTTP_204_NO_CONTENT)