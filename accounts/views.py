from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def add_user(request):
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			u = form.save()
			u.set_password(u.password)
			u.save()
			return redirect('user_login')
	else:
		form = UserForm()
	return render(request, 'accounts/add_user.html',{'form':form})

def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user:
			login(request,user)
			return redirect('/')
		else:
			messages.error(request, 'usuário ou senha invalidos!')
	return render(request, 'accounts/login.html')

def logout_user(request):
	logout(request)
	return redirect('user_login')