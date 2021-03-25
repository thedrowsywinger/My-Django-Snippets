from django.shortcuts import render, redirect
from django.http import HttpResponse


########################### For Email ###########################
from RegularDjango.mail import send_email
#################################################################

# Create your views here.

def HomeView(request):

    return render(request, "landing/home.html")




def sendmail(request):
    send_email()
    print("Done")
    return HttpResponse("Go Check Email")