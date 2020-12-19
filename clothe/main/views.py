from main.utils import getAPICall
from main.models import Post, Profile
from django.shortcuts import render, HttpResponse, redirect
from .forms import signupForm
from django.contrib.auth import authenticate, login
from .utils import *
from requests import get
from bs4 import BeautifulSoup

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

def profile_view(request):
    profile = Profile.objects.get(user=request.user)
    context = {
        'profile':profile,
    }

    return render(request, 'profile.html', context)

def preferences(request):
    return render(request, "preferences.html")
    
def userChoices(request):
    location = request.POST['location']
    gender = request.POST['gender']
    color_ = request.POST['color']
    URL = f'https://www.htmlcsscolor.com/hex/{color_[1:]}'
    response = get(URL)
    simple_soup = BeautifulSoup(response, 'html.parser')      # use html.parser in order to understand the simple HTML
    mydivs = simple_soup.find("h2", {"id": "cntMain_lblTints"})
    answer = mydivs.find('strong').getText()
    clothing_type = request.POST['clothing_type']
    style = request.POST['style']
    upper = int(request.POST['upper'])
    lower = int(request.POST['lower'])
    search_results = getAPICall(location, gender, answer, clothing_type, style, upper, lower)
    print(search_results)
    return render(request, 'search_results.html', {'search_results':search_results})

def post_comment_create_and_list_view(request):
    qs = Post.objects.all()
    profile = Profile.objects.get(user=request.user)
    context = {
        'qs':qs,
        'profile':profile,
    }

    return render(request, 'post.html', context)

def like_unlike_post(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Post.objects.get(id=post_id)
        profile = Profile.objects.get(user=user)

        if profile in post_obj.liked.all():
            post_obj.liked.remove(profile)
        else:
            post_obj.liked.add(profile)
        
        like, created = Like.objects.get_or_create(user=profile, post_id=post_id)

        if not created:
            if like.value == 'Like':
                like.value='Unlike'
            else:
                like.value='Like'

        else:
            like.value='Like'
            
            post_obj.save()
            like.save()
    return redirect('posts')