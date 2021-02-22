from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from custom_authentication.forms import SignupForm, CustomUserForm

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
			current_user = User.objects.get(email=request.POST['business_email'])
			# current_user.is_active = False
			# current_user.save()
            
			
			current_user_profile = profile_form.save(commit = False)
			current_user_profile.user = current_user
			current_user_profile.save()
			
			return HttpResponse("SignUp was successful")

		else:
			print("Error in Signup")
			print(signup_form.errors)
			return redirect('landing:home')

	return render(request, 'accounts/sign-up.html') 