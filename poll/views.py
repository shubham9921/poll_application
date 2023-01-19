from django.shortcuts import render
from .forms import CreatePollForm
from django.shortcuts import redirect
from .models import Poll
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.contrib import auth


def home(request):
    polls = Poll.objects.all()

    context = {
        'polls' : polls
    }
    return render(request, 'poll/home.html', context)

def create(request):
    form = CreatePollForm(request.POST)

    if form.is_valid():
        form.save()
    return redirect('home')

def results(request):
    context = {}
    return render(request, 'poll/results.html', context)

def vote(request):
    context = {}
    return render(request, 'poll/vote.html', context)


def create(request):
    if request.method == 'POST':
        form = CreatePollForm(request.POST)
    else:
        form = CreatePollForm()

    context = {'form' : form}
    return render(request, 'poll/create.html', context)

def welcome(request):
    return render(request,'welcome.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        password = request.POST['password']
        x=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,password=password)
        x.save()
        print("USER CREATED")
        return redirect('/welcome/')
    return render(request,'signup.html')



def login(request):
    if request.session.has_key('is_logged'):
        return redirect("/home/")
    if request.method == 'POST':
        username1 = request.POST['username']
        password1 = request.POST['password']
        user=auth.authenticate(username=username1,password=password1)
        if user is None:
            return redirect('/login/')
        else:
            request.session['is_logged']=True
            return redirect('/home/')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/welcome/')
