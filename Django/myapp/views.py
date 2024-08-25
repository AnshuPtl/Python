from django.shortcuts import render,redirect
from .models import User ,Category
from django.conf import settings
from django.core.mail import send_mail
import random
# Create your views here.

def index(request):
	return render(request,'index.html')

def seller_index(request):
	return render(request,'seller_index.html')

def seller_addproduct(request):
	category=Category.objects.all()
	return render(request,'seller_addproduct.html',{'cat': category})

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
				usertype=request.POST['usertype'],
				)
			msg1="Registration Successfull"
			return render(request,'Signup.html',{'msg1':msg1})

	else:
		return render(request,'Signup.html')

def login(request):
	if request.method=="POST":
		try:
			user=User.objects.get(email=request.POST['email'],pswd=request.POST['pswd'])
			
			if user.usertype=="seller":
				request.session['email']=user.email
				request.session['name']=user.name
				return render(request,'seller_index.html')

			else:
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

def forgotpswd(request):
	if request.method=="POST":
		try:
			user=User.objects.get(email=request.POST['email'])
			subject = 'OTP for forgot password'
			otp=random.randint(1000,9999)
			message = f'Hi {user.name}, Your OTP is: '+str(otp)
			email_from = settings.EMAIL_HOST_USER
			recipient_list = [user.email, ]
			send_mail( subject, message, email_from, recipient_list )

			return render(request,'verifyotp.html',{'email':user.email, 'otp':otp})
		
		except:
			msg = "No such User Exist !!!"
			return render(request,'forgotpswd.html',{'msg':msg})
	else:
		return render(request,'forgotpswd.html')

def verifyotp(request):
	if request.method=='POST':
		email=request.POST['email']
		otp=request.POST['otp']
		uotp=request.POST['uotp']
		
		if otp == uotp:
			return render(request,'createpswd.html',{'email' : email})
		else:
			msg="OTP Doesn't Matched !!!"
			return render(request,'verifyotp.html',{'msg': msg})

	else:
		return render(request,'verifyotp.html')

def createpswd(request):
	if request.method=="POST":
		try:
			user=User.objects.get(email=request.POST['email'])
			if request.POST['npswd']==request.POST['cnpswd']:
				user.pswd=request.POST['npswd']
				user.save()
				return redirect('login')
			else:
				msg="New Password & Confirm Password Doesn't Matched !!!"
				return render(request,'createpswd.html',{'msg':msg})

		except:
			return render(request,'createpswd.html')
	else:
		return render(request,'createpswd.html')


def schngpswd(request):
	if request.method=="POST":
		try:
			seller=User.objects.get(email=request.session['email'],)
			if seller.pswd==request.POST['opswd']:
				if request.POST['npswd']==request.POST['cnpswd']:
					seller.pswd=request.POST['npswd']
					seller.save()
					return redirect('logout')
				else:
					msg="New Password & Confirm New Password Doesn't Matched !!!"
					return render(request,"schngpswd.html",{'msg':msg})
			
			else:
				msg="Old Password Doesn't Matched !!!"
				return render(request,"schngpswd.html",{'msg':msg})
	
		except:
			msg="Something went wrong !!!"
			return render(request,"schngpswd.html",{'msg':msg})

	else:
		return render(request,'schngpswd.html')
