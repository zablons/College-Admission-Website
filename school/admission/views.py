from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your views here.
@login_required(login_url='login')
def Index(request):
    return render(request, 'index.html')

def Signin(request):
   if request.method == 'POST':
        username = request.POST['username']
        #id = request.POST['adm_no']
        password1 = request.POST['password1']

        user = authenticate(request, username=username, password=password1)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid login details')
            return redirect('login')
    
   return render(request, 'signup.html')

def Signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        #id = request.POST['adm_no']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        #input validation
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exist!')
            return redirect('register')
        
        if User.objects.filter(email=email).exists():
                  messages.error(request, 'Email already in use!')
                  return redirect('register')  
        
        '''if User.objects.filter(id=id).exists():
                  messages.error(request, 'Admission already in use!')
                  return redirect('register')'''  
        
        if not username.isalnum():
            messages.error(request, 'Username cannot contain special characters or symbols')
            return redirect('register')
        
        if password1 != password2:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
        
        myuser = User.objects.create_user(username, email, password1)
        myuser.save()

        messages.success(request, "Account created successfully.")
          
        return redirect('register')

    return render(request, 'signup.html')

def Signout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def Upload(request):
    if request.method == 'POST':
        image_file = request.FILES.get('image')
        if image_file:
            profile = request.user.profile
            profile.image = image_file
            profile.save()
            return redirect('profile')
    return render(request, 'profile.html')


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)