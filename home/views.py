from django.shortcuts import render
from .forms import RegistrationForm
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.shortcuts import redirect

# Create your views here.
def index(request):
   return render(request, 'pages/home.html')

def contact(request): 
   return render(request, 'pages/contact.html')

def error(request, *args, **kwargs):
   return render(request, 'pages/error.html')

def register(request):
   form = RegistrationForm()
   if request.method == 'POST':
      form = RegistrationForm(request.POST)
      if form.is_valid():
         form.save()
         return HttpResponseRedirect('/')
   return render(request, 'pages/register.html', {'form': form})



