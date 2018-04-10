from django.shortcuts import render
# hash 
from passlib.hash import pbkdf2_sha256

from FORMVALIDATION.models import User
# for httpResponse
from django.http import HttpResponse
# jason response
from django.http import JsonResponse

def show_form(request):
	return render(request, 'FormValidation/mainpage/form.html') 



# login 
def login(request):
	# form-name 
	if(request.method == "POST"):
		email = request.POST['email'];
		password = request.POST['password']

		return HttpResponse(email, password)
	else:
		return HttpResponse('do something')




# signup
def signup(request):
	if(request.method == "POST"):
		name = request.POST['name']
		email = request.POST['email']
		password = request.POST['password']



		return HttpResponse(name, email, password)

def validate_email(request):
	email = request.GET.get('email', None)
	data = {
		'is_taken': "FUCK YOU"
	}
	return JsonResponse(data)


def sendRandomNum(request):
	import random
	num = random.randint(0,1000)

	NUMBER = {
		'num': num
	}

	return JsonResponse(NUMBER)


