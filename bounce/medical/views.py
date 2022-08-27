from .models import student_Inf
from django.shortcuts import redirect, render
from .forms import Request_info 
from django.core.files.storage import FileSystemStorage

def index(request):
    context = {}
    if request.method == 'POST':
        upload_file = request.FILES['document']
        fs = FileSystemStorage()
        name =fs.save(upload_file.name, upload_file)
        # if form.is_valid():
        #     form.save()
        #     return redirect('thank')
        context = {
            'url' :fs.url(name)
            }
    return render(request , 'medical/index.html', context) 

def upload_data(request):
    if request.method =='POST':
        form = Request_info(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect('thank')
    else:
        form = Request_info()
    context ={
        'form':form
    }
    return render(request ,'medical/upload.html' , context)
  
def thanks(request):
    return render(request ,'medical/time.html') 
