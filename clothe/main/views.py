from main.utils import getAPICall
from main.models import Post, Profile
from .utils import getAPICall
from .models import Post, Profile
from .models import *
from django.shortcuts import render, HttpResponse, redirect
from .forms import *
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

def editProfile(request):
    profile = Profile.objects.get(user=request.user)
    context = {
        'profile':profile,
    }
    return render(request, 'edit_profile.html', context)

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
    
def create_posts(request):
    profile = Profile.objects.get(user=request.user)

    # Post form, comment form
    p_form = PostModelForm(request.POST or None, request.FILES or None)

    if p_form.is_valid():
        instance = p_form.save(commit=False)
        instance.author = profile
        instance.save()
        return redirect('posts')
    
    context = {
        'profile':profile,
        'p_form':p_form,
    }

    return render(request, 'newpost.html', context)

def post_comment_create_and_list_view(request):
    qs = Post.objects.all()
    profile = Profile.objects.get(user=request.user)


    # Post form, comment form
    p_form = PostModelForm(request.POST or None, request.FILES or None)

    if p_form.is_valid():
        instance = p_form.save(commit=False)
        instance.author = profile
        instance.save()
        p_form = PostModelForm()

    context = {
        'qs':qs,
        'profile':profile,
        'p_form':p_form,
    }

    print(qs)
    for post in qs:
        print(post.num_likes)
    print(profile)

    return render(request, 'posts.html', context)

def like_unlike_post(request):
    user = request.user
    print("HERE NOW")
    if request.method == 'POST':
        data = json.loads(request.body)
        post_id = data['id']
        print("HERE")
        print(post_id)
        post_obj = Post.objects.get(id=post_id)
        profile = Profile.objects.get(user=user)

        if profile in post_obj.liked.all():
            post_obj.liked.remove(profile)
        else:
            post_obj.liked.add(profile)
            if profile in post_obj.disliked.all():
                post_obj.disliked.remove(profile)
                print("HERESOUJHFOIUSHEF")
        
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
def login(request):
    return render(request, "login.html")
def dislike_undislike_post(request):
    user = request.user
    if request.method == 'POST':
        print("HERE")
        data = json.loads(request.body)
        post_id = data['id']
        print("HERE")
        print(post_id)
        post_obj = Post.objects.get(id=post_id)
        profile = Profile.objects.get(user=user)

        if profile in post_obj.disliked.all():
            post_obj.disliked.remove(profile)
            print("HERESOUJHFOIUSHEF")
        else:
            post_obj.disliked.add(profile)
            if profile in post_obj.liked.all():
                post_obj.liked.remove(profile)
        
        dislike, created = Dislike.objects.get_or_create(user=profile, post_id=post_id)

        if not created:
            if dislike.value == 'Dislike':
                dislike.value='Undislike'
            else:
                dislike.value='Dislike'

        else:
            dislike.value='Dislike'
            
            post_obj.save()
            dislike.save()
    return redirect('posts')

