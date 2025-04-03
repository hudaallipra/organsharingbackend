
from django.urls import include, path

from .views import *

urlpatterns = [
    path('login', Loginpage.as_view(), name='login'),
    path('add doctor',AddDoc.as_view(),name='add doctor'),
    path('view doctor',ViewDoc.as_view(),name='view doctor'),
    path('organ request',ViewOrgReq.as_view(),name='organ request'),
    path('assign doc',AssignDoc.as_view(),name='assign doc'),
    path('view organ donation',ViewOrgDon.as_view(),name='view organ donation'),
    path('manage hospital location',ManageHosLoc.as_view(),name='manage hospital location'),
    path('view user details',ViewUserDet.as_view(),name='view user details'),
    path('admin dashboard',AdminDash.as_view(),name='admin dashboard'),
    path('new request',NewReq.as_view(),name='new request'),
    path('organ collection',OrganCo.as_view(),name='organ collection'),
    path('patient list',PatientList.as_view(),name='patient list'),
    path('schedule appointments',Sched.as_view(),name='schedule appointments'),
    path('doctor dashboard',DocDash.as_view(),name='doctor dashboard')
]
