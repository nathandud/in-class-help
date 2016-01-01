from django.db import models

# Create your models here.

class ClassroomLayout(models.Model):
    file_upload = models.ImageField(upload_to='layouts/')
    filename = models.TextField(max_length=30)
    # mime_type = models.TextField(max_length=20)
    title = models.TextField(max_length=30)

    def __str__(self):
        return self.title

class StudentLocation(models.Model):
    xcoord = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    ycoord = models.DecimalField(max_digits=10, decimal_places=2, default =0)
    img_width = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    img_height = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return '{}, {}'.format(self.xcoord, self.ycoord)

class Ticket(models.Model):
    time = models.DateTimeField(auto_now=True)
    student_question = models.TextField(default="")
    completed = models.BooleanField(default=False)
    location = models.OneToOneField(StudentLocation, primary_key=False)

    def __str__(self):
        return self.id
        
