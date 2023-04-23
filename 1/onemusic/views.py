from django.shortcuts import render,redirect
from .models import User

# Create your views here.
def index(request):
	return render(request,'index.html')

def signup(request):
	if request.method == "POST":
		try:
			User.objects.get(Email=request.POST['email'])
			msg="User Already Registered !!!"
			return render(request,'signup.html',{'msg':msg})
		except:
			User.objects.create(
				Name = request.POST['Name'],
				Email = request.POST['email'],
				PhoneNumber = request.POST['Phone Number'],
				Password = request.POST['password'],
				)
			msg2="Registration Successfull"
			return render(request,'login.html',{'msg2':msg2})
	else:
		return render(request,'signup.html')

def login(request):
	if request.method=="POST":
		Email=request.POST.get('email')
		pwd=request.POST.get('password')
		try:
			user=User.objects.get(Email=request.POST['email'],Password = request.POST['password'])
			request.session['email']=Email
			request.session['password']=pwd
			msg="Login Successfull"
			return render(request,'index.html',{'msg':msg})

		except:
			msg1="Email or Password is Invalid"
			return render(request,'login.html',{'msg1': msg1})

	else:
		return render(request,'login.html')

def logout(request):
	request.session.clear()
	return redirect('login')

def albums(request):
	return render (request,'albums-store.html')

def event(request):
	return render(request,'event.html')

def news(request):
	return render(request,'blog.html')

def contact(request):
	return render(request,'contact.html')

def changepswd(request):
	return render(request,'changepswd.html')