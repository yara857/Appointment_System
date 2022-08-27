from django.db import models
from django.forms.widgets import DateInput
import datetime

class time(models.Model):
    timer = models.DateTimeField(null=True)
    def __str__(self) :
        return str(self.timer)

class student_Inf(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField()
    std_id = models.CharField(max_length=25)
    national_id = models.CharField(max_length=4)
    phone_num = models.CharField(max_length=25)
    upload = models.FileField(upload_to="files")
    time_choice = models.ManyToManyField(time)
    def __str__(self):
        return self.national_id

    
    