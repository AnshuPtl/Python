from django.shortcuts import render,redirect
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

def login(request):
	if request.method=="POST":
		try:
			user=User.objects.get(email=request.POST['email'],pswd=request.POST['pswd'])
			request.session['email']=user.email
			request.session['name']=user.name
			return render(request,'index.html')

		except:
			msg1="Email or Password is Invalid"
			return render(request,'login.html',{'msg1': msg1})
			
	else:
		return render(request,'login.html')

def logout(request):
	try:
		del request.session['email']
		del request.session['name']
		return render(request,'login.html')
	except:
		msg="Something went wrong, Try Again !!!"
		return render(request,'login.html',{'msg':msg})

def chngpswd(request):
	if request.method=="POST":
		try:
			user=User.objects.get(email=request.session['email'],)
			if user.pswd==request.POST['opswd']:
				if request.POST['npswd']==request.POST['cnpswd']:
					user.pswd=request.POST['npswd']
					user.save()
					return redirect('logout')
				else:
					msg="New Password & Confirm New Password Doesn't Matched !!!"
					return render(request,"chngpswd.html",{'msg':msg})
			
			else:
				msg="Old Password Doesn't Matched !!!"
				return render(request,"chngpswd.html",{'msg':msg})
	
		except:
			msg="Something went wrong !!!"
			return render(request,"chngpswd.html",{'msg':msg})

	else:
		return render(request,'chngpswd.html')

def profile(request):
	return render(request,'profile.html')
