from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import NewUserForm

#homepage for membership
def homepage(request):
  return HttpResponse("this is homepage")
  
# Create your views here.
def register_request(request):
  if request.method == "POST":
    form = NewUserForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      messages.success(request, "registration success")
      return redirect("membership:homepage")
    messages.errors(request, "registration failed")
  form = NewUserForm()
  return render(request=request, template_name="register.html", context={"form":form})

def login_request(request):
  if request.method == "POST":
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
      username = form.cleaned_data.get("username")
      password = form.cleaned_data.get("password")
      user = authenticate(username=username, password=password)
      if user is not None:
        login(request, user)
        print('login success', username)
        return redirect("membership:homepage")
    messages.error(request, "loggin failed. Invalid username or password")  
  form = AuthenticationForm()
  return render(request=request, template_name="login.html", context={"form":form})