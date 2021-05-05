from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from custom_authentication.forms import SignupForm, CustomUserForm

############### FOR PASSWORD RESET ###############

from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes

############### FOR PASSWORD RESET ###############

def SignUpView(request):
	if request.method == 'POST':
		data_for_signup = {
			'first_name' : request.POST['first_name'],
			'last_name' : request.POST['last_name'],
			'email' : request.POST['email'],
			'password1' : request.POST['password1'],
			'password2' : request.POST['password2']
		}
		data_for_profile = {
			'first_name' : request.POST['first_name'],
			'last_name' : request.POST['last_name'],
			'email' : request.POST['email'],
			'contact_number': request.POST['contact_number']
		}

		print(data_for_profile)

		signup_form = SignupForm(data_for_signup)
		profile_form = CustomUserForm(data_for_profile)

		if signup_form.is_valid():
			print("Everything is valid")
			signup_form.save()
			current_user = User.objects.get(email=request.POST['email'])
			# current_user.is_active = False
			# current_user.save()
            
			
			# current_user_profile = profile_form.save(commit = False)
			# current_user_profile.user = current_user
			# current_user_profile.save()
			
			return HttpResponse("SignUp was successful")

		else:
			print("Error in Signup")
			print(signup_form.errors)
			return redirect('landing:home')

	return render(request, 'accounts/sign-up.html') 


def LoginView(request):

	print("In the login view")

	if "login" in request.POST:

		email = request.POST.get('email')
		password = request.POST.get('password')

		current_user = User.objects.get(email=request.POST['email'])
		current_user_username = current_user.username

		user = authenticate(request, email=email, password=password)

		if user is not None:
			login(request, user)
			print("Login Successful")
			return HttpResponse("You are now logged in")
			# return redirect('user_profiles:profile')
		else:
			print("No user found")

			return redirect('landing:home')

	return render(request, 'accounts/log-in.html')

def LogoutView(request):

	logout(request)
	return	redirect('accounts:userlogin')


def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "registration/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'MyDjangoSnippets',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return render(request, "registration/password_reset_done.html")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="registration/password_reset.html", context={"password_reset_form":password_reset_form})



# def password_reset_request(request):
	