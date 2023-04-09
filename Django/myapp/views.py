from django.shortcuts import render
from .models import User
# Create your views here.

def index(request):
	return render(request,'index.html')

def about(request):
	return render(request,'about.html')
	
def contact(request):
	return render(request,'contact.html')

def products(request):
	return render(request,'products.html')

def feedback(request):
	return render(request,'feedback.html')

def signup(request):
	if request.method=="POST":
		try:
			user=User.objects.get(email=request.POST['email'])
			print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>> USING GET METHOD:: ",user)
			msg="User already exists !!!"
			return render(request,'Signup.html',{'msg':msg})

		except:
			User.objects.create(
				name=request.POST['name'],
				email=request.POST['email'],
				pswd=request.POST['pswd'],
				)
			msg1="Registration Successfull"
			return render(request,'Signup.html',{'msg1':msg1})

	else:
		return render(request,'Signup.html')
