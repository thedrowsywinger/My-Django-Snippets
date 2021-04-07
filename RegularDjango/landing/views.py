from django.shortcuts import render, redirect
from django.http import HttpResponse


########################### For Email ###########################
from RegularDjango.mail import send_email # For the one being sent to the visitor
from RegularDjango import secrets
from django.core.mail import send_mail, EmailMessage # For the one being sent to self
from django.conf import settings
from django.template.loader import render_to_string
#################################################################

# Create your views here.

def HomeView(request):

    return render(request, "landing/home.html")

def sendmail(request):

    send_email()
    print("Email sent to Visitor")

    data = {
        'message': 'This is a custom message, perhaps using the description/query of what the visitor wants sent directly to email instead of admin requiring to access the admin panel',
        'visitor': 'Hinata'
    }

    from_email = secrets.EMAIL_HOST_USER

    recipient_list = ['abdullah.md.sarwar@gmail.com']
    subject = render_to_string('landing/email/admin_email_subject.html', data).strip()
    html_message = render_to_string('landing/email/admin_email_body.html', data).strip()
    email = EmailMessage(subject, html_message, from_email, recipient_list)
    # email.attach_file('landing/static/landing/images/email.jpg')
    email.send()
    print("Email sent to admin")

    return HttpResponse("Go Check Email")