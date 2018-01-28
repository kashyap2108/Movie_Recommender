from django.shortcuts import render , HttpResponseRedirect , redirect
from django.contrib.auth.forms import UserCreationForm , PasswordChangeForm
from django.contrib.auth import login , authenticate , update_session_auth_hash
from django.core.urlresolvers import reverse
from .forms import SignupForm


def home(request):
	return render(request,'home.html',{})

def signup(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)
		print("hello",form.is_valid())
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password1')
			print(username,password)
			user = authenticate(username=username,password=password)
			login(request,user)
			return redirect('accounts:home')
	else:
		form = SignupForm()
	
	return render(request,'signup.html',{'form':form})

def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(request.user,request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request,user)
			messages.success(request,'Your password was successfully updated!!')
			return  redirec('change_password')
		else:
			messages.error(request,'Please correct the error below!')

	else:
		form = PasswordChangeForm(request.user)
	return render(request,'password_change.html',{'form':form})