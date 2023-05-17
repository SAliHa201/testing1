from django.shortcuts import render
from . models import Contact
# Create your views here.
def home(request):
    return render(request,'page/home.html')#no need to include template in the path
def about(request):
    return render(request,'page/about.html')
def contact(request):
    if request.method =="POST":
       #1 get the data from the form
       v_name= request.POST.get('name')
       v_email =request.POST.get('email')
       v_subject =request.POST.get('subject')
       v_massege =request.POST.get('massege')
    #2: send this date to the DB (Models))
       v_contact= Contact(name=v_name ,email=v_email, subject=v_subject,massege=v_massege )
       v_contact.save()
       return render(request,'page/thank.html')
    else:
       return render(request, 'page/contact.html')


