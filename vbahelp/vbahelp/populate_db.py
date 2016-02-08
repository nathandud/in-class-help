# !/usr/bin/env python3
import os
import django
os.environ["DJANGO_SETTINGS_MODULE"] = "vbahelp.settings"
django.setup()

print("HELP")

from vbahelp.locate import models as lmod

try:
    student1 = lmod.Student.objects.get(username='cschow')
except lmod.Student.DoesNotExist:
    student1 = Student()
    student1.user.username = "cschow"
    student1.user.first_name = "Caitlin"
    student1.last_name = "Dudley"
    student1.is_staff = False
    student1.save()
