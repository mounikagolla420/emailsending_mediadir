from django.shortcuts import render
from app.models import *
from app.forms import *
from django.http import HttpResponse
from django.core.mail import send_mail
# Create your views here.
def registration(request):
    ufo=UserForm()
    pfo=ProfileForm()
    d={'ufo':ufo,'pfo':pfo}

    if request.method=='POST' and request.FILES:
        ufd=UserForm(request.POST)
        pfd=ProfileForm(request.POST,request.FILES)
        if ufd.is_valid() and pfd.is_valid():
            NUFO=ufd.save(commit=False)
            password=ufd.cleaned_data['password']
            NUFO.set_password(password)
            NUFO.save()

            NPDO=pfd.save(commit=False)
            NPDO=username=NUFO
            NPDO.save()


            send_mail(
                'friendship letter',
                'sreenu is my best friend', 
                'mounikagolla2002@gmail.com',
                [NUFO.email],
                fail_silently=False)
            return HttpResponse('registraion is successfully')
        else:
            return HttpResponse('data is not valid')

    
    return render(request,'registration.html',d)