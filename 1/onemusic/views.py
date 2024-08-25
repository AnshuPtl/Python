from django.shortcuts import render,redirect
from .models import User,Product,Wishlist
from django.conf import settings
from django.core.mail import send_mail
import random

def index(request):
	return render(request,"index.html")

def seller_index(request):
	return render(request,"seller_index.html")

def about(request):
	return render(request,"about.html")

def blog(request):
	return render(request,"blog.html")

def events(request):
	products=Product.objects.all()
	return render(request,"events.html",{'products':products})

def contacts(request):
	return render(request,"contacts.html")

def login(request):
	if request.method=="POST":
		try:
			user=User.objects.get(email=request.POST['email'])
			print(user.usertype)
			if user.usertype=="User":
				request.session['email']=user.email
				request.session['fname']=user.fname
				wishlists=Wishlist.objects.filter(user=user)
				request.session['wishlist_count']=len(wishlists)
				return render(request,"index.html")

			else:
				request.session['email']=user.email
				request.session['fname']=user.fname
				return render(request,"seller_index.html")

		except Exception as e:
			print(e)
			msg1="Email or Password Does Not Matched!!!"
			return render(request,"login.html",{'msg1':msg1})

	else:
		return render(request,"login.html")

def signup(request):
	if request.method=="POST":
		try:
			User.objects.get(email=request.POST['email'])
			msg1="Email Already Exist"
			return render(request,"signup.html",{'msg1':msg1})

		except:
			if request.POST['password'] == request.POST['cpassword']:
				User.objects.create(
					fname=request.POST['fname'],
					lname=request.POST['lname'],
					mobile=request.POST['mobile'],
					email=request.POST['email'],
					address=request.POST['address'],
					password=request.POST['password'],
					usertype=request.POST['usertype']
				)

				msg="Sign Up Successful"
				return render(request,"signup.html",{'msg':msg})

			else:
				msg1="Password and Confim Password Does Not Matched !!!"
				return render(request,"signup.html",{'msg1':msg1})

	else:
		return render(request,"signup.html")


def logout(request):

	try:

		del request.session['email']
		del request.session['fname']
		del request.session['wishlist_count']
		return render(request,'login.html')
	
	except:

		return render(request,'login.html')


def change_password(request):
	if request.method=="POST":
		user=User.objects.get(email=request.session['email'])

		if user.password==request.POST['old_password']:
			if request.POST['new_password']==request.POST['cnew_password']:
				user.password=request.POST['new_password']
				user.save()
				return redirect('logout')

			else:
				msg1="New Password & Confirm New Passwrd Does Not Matched !!!"
				return render(request,'change_password.html',{'msg1':msg1})

		else:
				msg1="Old Passwrd Does Not Matched !!!"
				return render(request,'change_password.html',{'msg1':msg1})

	else:
		return render(request,'change_password.html')


def forgot_password(request):
	if request.method=="POST":
		try:
			print(request.POST['email'])
			user=User.objects.get(email=request.POST['email'])
			otp = random.randint(1000,9999)
			subject = 'OTP - Forgot Password'
			message = "Hello "+user.fname+ ", Your OTP : "+str(otp)
			email_from = settings.EMAIL_HOST_USER
			recipient_list = [user.email,]
			send_mail( subject, message, email_from, recipient_list )
			msg="OTP Sent Successful"
			return render(request,'verify_otp.html',{'email':user.email,'otp':otp,'msg':msg})

		except Exception as e:
			print(e)
			print("Hello1")
			msg1="Email Does Not Exist !!!"
			return render(request,'forgot_password.html',{'msg1':msg1}) 

	else:
		return render(request,'forgot_password.html')


def verify_otp(request):
	email=request.POST['email']
	otp=request.POST['otp']
	uotp=request.POST['uotp']

	if otp==uotp:
		return render(request,'new_password.html',{'email':email})

	else:
		msg1="OTP Does Not Matched !!!"
		return render(request,'verify_otp.html',{'email':email, 'otp':otp,'msg1':msg1})


def new_password(request):
	email=request.POST['email']
	np=request.POST['new_password']
	cnp=request.POST['cnew_password']

	if np==cnp:
		user = User.objects.get(email=email)
		user.password=np
		user.save()

		return redirect('login')

	else:
		msg1="New Password & Condirm New password Does Not 'Matched !!!"
		return render(request,'new_password.html',{'email':email, 'msg1':msg1})

def seller_change_password(request):
	if request.method=="POST":
		user=User.objects.get(email=request.session['email'])

		if user.password==request.POST['old_password']:
			if request.POST['new_password']==request.POST['cnew_password']:
				user.password=request.POST['new_password']
				user.save()
				return redirect('logout')

			else:
				msg1="New Password & Confirm New Passwrd Does Not Matched !!!"
				return render(request,'seller_change_password.html',{'msg1':msg1})

		else:
				msg1="Old Passwrd Does Not Matched !!!"
				return render(request,'seller_change_password.html',{'msg1':msg1})

	else:
		return render(request,'seller_change_password.html')


def seller_add_product(request):

	if request.method=="POST":
		seller=User.objects.get(email=request.session['email'])
		Product.objects.create(
				seller=seller,
				product_name=request.POST['product_name'],
				product_price=request.POST['product_price'],
				product_qty=request.POST['product_qty'],
				product_desc=request.POST['product_desc'],
				product_image=request.FILES['product_image'],
				product_venue=request.POST['venue'],
				product_time=request.POST['time'],
				product_date=request.POST['date'],
			)

		msg="Product Added Successfully"
		print(msg)
		return render(request,'seller_add_product.html',{'msg':msg})

	else:
		return render(request,'seller_add_product.html')

def seller_view_product(request):
	seller=User.objects.get(email=request.session['email'])
	products=Product.objects.filter(seller=seller)
	return render(request,'seller_view_product.html',{'products':products})

def seller_product_detail(request,pk):
	product=Product.objects.get(pk=pk)
	return render(request,'seller_product_detail.html',{'product':product})

def seller_product_edit(request,pk):
	product=Product.objects.get(pk=pk)
	if request.method=="POST":
		product.product_name=request.POST['product_name']
		product.product_desc=request.POST['product_desc']

		try:
			product.product_image=request.FILES['product_image']
			product.product_qty=request.POST['product_qty']
			product.product_price=request.POST['product_price']
			product.product_venue=request.POST['product_venue']
			product.product_date=request.POST['product_date']
			product.product_time=request.POST['product_time']

		except:
			pass
		
		product.save()
		msg="Concert Updated Successfully"
		return render(request,'seller_product_detail.html',{'product':product, 'msg':msg})

	else:
		return render(request,'seller_product_edit.html',{'product':product})

def seller_product_delete(request,pk):
	product=Product.objects.get(pk=pk)
	product.delete()
	return redirect('seller_view_product')

def product_detail(request,pk):
	wishlist_flag=False
	product=Product.objects.get(pk=pk)
	user=User.objects.get(email=request.session['email'])
	try:
		Wishlist.objects.get(user=user,product=product)
		wishlist_flag=True
	except:
		pass

	return render(request,'product_detail.html',{'product':product,'wishlist_flag':wishlist_flag,'cart_flag':cart_flag})

def wishlist(request):
	user=User.objects.get(email=request.session['email'])
	wishlists=Wishlist.objects.filter(user=user)
	request.session['wishlist_count']=len(wishlists)
	return render(request,'wishlist.html',{'wishlists':wishlists})

def add_to_wishlist(request,pk):
	product=Product.objects.get(pk=pk)
	user=User.objects.get(email=request.session['email'])
	Wishlist.objects.create(user=user,product=product)

	return redirect('wishlist')

def remove_from_wishlist(request,pk):

	product=Product.objects.get(pk=pk)
	user=User.objects.get(email=request.session['email'])
	Wishlist.objects.get(user=user,product=product).delete()

	return redirect('wishlist')