from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ClassroomLayout(models.Model):
    file_upload = models.ImageField(upload_to='layouts/')
    filename = models.TextField(max_length=30)
    # mime_type = models.TextField(max_length=20)
    title = models.TextField(max_length=30)

    def __str__(self):
        return self.title

class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True

class Student(Person):
    major = models.TextField(max_length=50)

    def __string__(self):
        return '{} {} ({})'.format(self.user.first_name, self.user.last_name,
            self.username)

class Ticket(models.Model):
    student = models.ForeignKey(Student)
    time = models.DateTimeField(auto_now=True)
    student_question = models.TextField(default="")
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.id

class StudentLocation(models.Model):
    ticket = models.ForeignKey(Ticket)
    xcoord = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    ycoord = models.DecimalField(max_digits=10, decimal_places=2, default =0)
    img_width = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    img_height = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return '{}, {}'.format(self.xcoord, self.ycoord)



'''
Django-provided fields
username
first_name
last_name
email
password
groups
user_permissions
is_staff
is_active
is_superuser
last_login
date_joined
'''
