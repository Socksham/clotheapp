from django.shortcuts import render, HttpResponse, redirect
from .forms import signupForm
from django.contrib.auth import authenticate, login
from .utils import *
# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup_view(request):
    print("signup")
    if request.method == 'POST':
        form = signupForm(request.POST) 
        print(form.is_valid())
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            print(user)
            login(request, user)
            return redirect('home')
    else:
        form = signupForm()

    return render(request, 'signup.html', {'form': form})

def preferences(request):
    return render(request, "preferences.html")
def userChoices(request):
    location = request.POST['location']
    gender = request.POST['gender']
    color_ = request.POST['color']
    clothing_type = request.POST['clothing_type']
    style = request.POST['style']
    upper = int(request.POST['upper'])
    lower = int(request.POST['lower'])
    search_results = getAPICall(location, gender, color_, clothing_type, style, upper, lower)
    print(search_results)
    return render(request, 'search_results.html', {'search_results':search_results})
