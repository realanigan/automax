from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login



def login_view(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        login_form = AuthenticationForm(request=request, data=request.POST)
        if login_form.is_valid():
            password = login_form.cleaned_data.get('password')
            user = login_form.get_user()
            print(password)
            login(request, user)
            return redirect('home')
            # username = login_form.cleaned_data.get('username')
            # password = login_form.cleaned_data.get('password')
            # user = authenticate(username=username,password=password)
        else:
            pass
            
        

    elif request.method == "GET":
        login_form = AuthenticationForm()

    return render(request, 'users/login.html', {"login_form": login_form})
