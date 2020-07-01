from django.shortcuts import render
from UserAuth.forms import UserForm,UserProfileInfoForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'UserAuth/index.html')

@login_required
def special(request):
    return HttpResponse("You are logged in , Nice!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileInfoForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            #here Password will be in plain text
            #print("Password is :" + user.password)
            user.set_password(user.password)
            user.save()
            #Password is being hashed here
            print("Password after Hash  is :" + user.password)
            #print("user name is :" + user.username)
            profile = profile_form.save(commit=False)
            #print('Profile is :' + profile.portfolio_site)
            profile.user = user
            #print('profile user is : ' + profile.user.password)

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'UserAuth/registration.html',{'user_form':user_form,
                                                    'profile_form':profile_form,
                                                    'registered':registered,})





def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account Not Active")
        else:
            print("Someone tried to login and failed!")
            print("Username: {} and password {}".format(username,password))
            return HttpResponse("Invalid login details supplied!")
    else:
        return render(request,'UserAuth/login.html', {})
