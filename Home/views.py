from django.shortcuts import render,HttpResponse
from matplotlib.style import context
from datetime import datetime
from Home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        "variable":"this is sent"
    }
    return render(request,'index.html', context)
    messages.success(request,"this message has been sent")
   # return HttpResponse("This is Homepage")
 

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("This is about page")

def services(request):
    return render(request, 'services.html')
    #return HttpResponse("This is service page")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('Phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your Message has been sent!')

    return render(request, 'contact.html')

    #return HttpResponse("This is contact page")
