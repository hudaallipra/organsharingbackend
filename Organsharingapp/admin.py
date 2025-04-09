from django.contrib import admin

from .models import *


# Register your models here.

admin.site.register(Logintable)
admin.site.register(Doctor)
admin.site.register(Usertable)
admin.site.register(OrganDonation)
admin.site.register(OrganRequest)
admin.site.register(Appointment)
admin.site.register(Organ)





