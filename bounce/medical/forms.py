from .models import student_Inf 
from django.forms import ModelForm

class Request_info(ModelForm):
      class Meta():
        model = student_Inf
        fields = ('name','mail','std_id','national_id','phone_num','upload','time_choice')