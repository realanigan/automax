from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views import View
from django.contrib.auth.decorators import login_required

def login_view(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        login_form = AuthenticationForm(request=request, data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            messages.success(request, f"You are now logged in as {user.username}")
            return redirect('home')
            # username = login_form.cleaned_data.get('username')
            # password = login_form.cleaned_data.get('password')
            # user = authenticate(username=username,password=password)
        else:
            messages.error(request, f"Unable to log in")

    elif request.method == "GET":
        login_form = AuthenticationForm()
    

    return render(request, 'users/login.html', {"login_form": login_form})


@login_required
def logout_view(request):
    logout(request)
    return redirect('main')

# def register_vieww(request):
#     register_form = UserCreationForm()
#     return render(request, 'views/register.html',{"register_form": register_form})



class RegisterView(View):

    def get(self, request):
        register_form = UserCreationForm()
        return render(request, 'views/register.html', {"register_form": register_form})
    
    def post(self, request):
        register_form = UserCreationForm(data=request.POST)
        if register_form.is_valid():
            user = register_form.save()
            user.refresh_from_db()
            login(request, user)
            messages.success(request, f"{user.username} registered successfully")
            return redirect('home')
       
        else:
            messages.error(request, "Registration failed. Please correct the errors below.")
            return render(request, 'views/register.html', {"register_form": register_form})



