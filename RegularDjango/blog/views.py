from django.shortcuts import render, redirect
from django.views.generic import View

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from blog.models import BlogUploaderModel

from blog.forms import UploadingForm

import json

from django.http import HttpResponse

# Create your views here

def BlogHomeView(request):
	blogs = BlogUploaderModel.objects.all()
	context = {
		'blogs': blogs,
	}
	return render(request, "blog/home.html", context)

def BlogEditorView(request):

	if request.method == "POST":
		print("post request incoming")
		
		# print("something",request.POST['something'])

		# print("savedData", request.POST.get('savedData', 'not really'))

		# print("data", request.POST['something'])

		incoming = json.loads(request.POST['something'])

		print(incoming)

		# model = BlogModel(

		# 	created_by=request.user.username,
		# 	blog_data = incoming

		# 	)

		# model.save()

		print("Save a success")

	return render(request, "blog/blog_editor.html")


def TestView(request):

	test = BlogUploaderModel.objects.all()[0]

	context = {
		'test': test
	}

	return render(request, 'blog/test.html', context)


def BlogUploaderView(request):

	if request.method == "POST":
		form = UploadingForm(request.POST, request.FILES)
		print("Am i here")
		if form.is_valid():
			print("All good")
			print(form)
			form.save()
			return HttpResponse("Blog Upload Successful")

		else:
			print(form.errors)

	else:
		form = UploadingForm()

	context = {
		'form': form
	}

	return render(request, "blog/blog_uploader.html", context)

def BlogEditorView(request, pk):

	blog = BlogUploaderModel.objects.get(pk=pk)
	form = UploadingForm(instance = blog)

	if "blog_edit" in request.POST:

		if request.method == "POST":
			form = UploadingForm(request.POST, instance = blog)
			print("Am i here")
			if form.is_valid():
				print("All good")
				form.save()
				return HttpResponse("Task Successful")

		else:
			form = UploadingForm(instance = blog)

	context = {
		'form': form
	}

	return render(request, "blog/blog_editor.html", context)

	
def BlogRemoverView(request, pk):
	
	blog = BlogUploaderModel.objects.get(pk=pk)
	blog.delete()

	return HttpResponse("Task Successful")

def BlogView(request, pk):

	blog = BlogUploaderModel.objects.get(pk=pk)
	
	context = {
		'blog':blog
		}

	return render(request, "blog/view_blog.html", context)