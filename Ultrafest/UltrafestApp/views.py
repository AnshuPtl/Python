from django.shortcuts import render
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
			msg1="Registration Successfull"
			return render(request,'signup.html',{'msg1':msg1})
	else:
		return render(request,'signup.html')