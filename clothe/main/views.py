from django.shortcuts import render, HttpResponse
from .forms import signupForm
from django.contrib.auth import authenticate, login

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
