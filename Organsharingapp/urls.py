from django.urls import path
from .views import *

urlpatterns = [
    # Web page views
    path('', Loginpage.as_view(), name='login'),
    path('adddoctor', AddDoc.as_view(), name='adddoctor'),
    path('DeleteDoc/<int:id>',DeleteDoc.as_view(),name='DeleteDoc'),
    path('editdoctor/<int:id>',EditDoc.as_view(),name='editdoctor'),
    path('viewdoctor', ViewDoc.as_view(), name='viewdoctor'),
    path('organ request', ViewOrgReq.as_view(), name='organ request'),
    path('organrequestupdate/<int:id>',organrequestupdate.as_view(),name='organrequestupdate'),
    path('assign doc', AssignDoc.as_view(), name='assign doc'),
    path('view organ donation', ViewOrgDon.as_view(), name='view organ donation'),
    path('manage hospital location', ManageHosLoc.as_view(), name=' hospmanageital location'),
    path('view user details', ViewUserDet.as_view(), name='view user details'),
    path('admindashboard', AdminDash.as_view(), name='admin dashboard'),
    path('new request', NewReq.as_view(), name='new request'),
    path('organ collection', OrganCo.as_view(), name='organ collection'),
    path('patient list', PatientList.as_view(), name='patient list'),
    path('schedule appointments', Sched.as_view(), name='schedule appointments'),
    path('doctor dashboard', DocDash.as_view(), name='doctor dashboard'),
    path('organrequestaccept/<int:id>/',organrequestaccept.as_view(),name='organrequestaccept'),
    path('organrequestreject/<int:id>/',organrequestreject.as_view(),name='organrequestreject'),

    # API endpoints
    path('LoginPageApi', LoginAPIView.as_view(), name='loginapi'),
    path('doctorapi', DoctorAPIView.as_view(), name='doctorapi'),
    path('userapi', UserAPIView.as_view(), name='userapi'),
    path('userapi/<int:pk>', UserAPIView.as_view(), name='userapi'),
    path('organdonationapi', OrganDonationAPIView.as_view(), name='organdonationapi'),
    path('organrequestapi', OrganRequestAPIView.as_view(), name='organrequestapi'),  # fixed typo in 'name'
    path('appointmentapi', AppointmentAPIView.as_view(), name='appointment'),
    path('donorregistrationapi',DonorRegistrationApi.as_view(),name='DonorRegistrationApi'),
    path('loginapi',LoginPageApi.as_view(),name='LoginPageApi'),
    #urls.py
    path('orgondonerlist', organ_donor_list.as_view(), name='organ-donor-list'),
    # path('vieworgans',vieworgans.as_view(),name='vieworgans')
    path('organdonation', OrganDonationAPI.as_view()),  # GET & POST
    path('organdonation/<int:pk>', OrganDonationAPI.as_view()),  
    path('organrequest', OrganRequestAPIView.as_view()),  # for get & post
    path('organrequest/<int:id>', OrganRequestAPIView.as_view()),  # for put & delete
    path('appointments/<int:pk>/', AppointmentDetail.as_view(), name='appointment-detail'),
    path('OrganDonorRequestAPIView/<int:id>',OrganDonorRequestAPIView.as_view(),name='OrganDonorRequestAPIView'),
    path('Appointmentlist',Appointmentlist.as_view(),name='Appointmentlist'),
    path('Appointmentupdate/<int:id>',Appointmentupdate.as_view(),name='Appointmentupdate'),

]
