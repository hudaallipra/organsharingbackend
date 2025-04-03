from django.contrib import admin

from .models import *


# Register your models here.

admin.site.register(Login)
admin.site.register(Doctor)
admin.site.register(User)
admin.site.register(PatientList)
admin.site.register(OrganDonation)
admin.site.register(OrganRequest)
admin.site.register(Appointment)





