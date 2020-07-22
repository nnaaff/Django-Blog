from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST) # passing user-submitted data into a new instance of UserCreationFrom 
        if form.is_valid(): # performs auth.n/valid.n on passed form and returns instance which is either valid/invalid
            user = form.save()
            login(request, user)
            return redirect('articles:list')
    
    elif request.method == 'GET':
        form = UserCreationForm()
    
    return render(request, 'accounts/signup.html', {'form': form}) 
    # executed either when it is a GET req, or when it is a POST req but user-submitted data is invalid
    # depending on req type, instance of 'form' rendered is either new blank / invalid post-auth.n


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid(): 
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))  # it's not a Django field - use '.get()' to access HTML field 
            else:
                return redirect('articles:list')
    
    else:
        form = AuthenticationForm()
    
    return render(request, 'accounts/login.html', {'form': form}) 


def logout_view(request):
    if request.method=='POST':
        logout(request)
        return redirect('articles:list')


