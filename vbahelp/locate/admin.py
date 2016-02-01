from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from locate.models import *

# Register your models here.
admin.site.register(ClassroomLayout)
admin.site.register(StudentLocation)
admin.site.register(Ticket)
