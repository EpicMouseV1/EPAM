from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm, Client_requests
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth import get_user_model
from .models import Request, Client
import datetime
User = get_user_model()

def login_client(request):
    if request.method == "POST":
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("index")  # Replace "index" with the name of the view you want to redirect to after a successful login
        else:
            messages.error(request, "Invalid email or password.")
    else:
        form = LoginForm()
        messages.error(request, "Invalid email or password.")

    return render(request, "base/login.html", context={"login_form": form})

def index(request):
    context = {}
    return render(request, 'base/index.html', context)

def register_client(request):

    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "ERROROROROOR")
    else:
        form = SignupForm()

    return render(request, 'base/register.html', context={"register_form":form})

def client_requests(request):
    context = {}
    if request.method == "POST":
        form = Client_requests(request.POST)
        context['request'] = form
        if request.user.is_authenticated:
            uid = request.user.id
            context['uid'] = uid
            if form.is_valid():
                req = form.save(commit=False)
                req.client_id = Client.objects.get(profile_id = uid)
                req.type = type = form.cleaned_data['type']
                req.comments = form.cleaned_data['comments']
                req.status ="new"
                req.open_date = datetime.datetime.now()
                req.save()
            else:
                messages.error(request, "ERROROROROOR")
        else:
            return redirect('index')
    else:
        form = Client_requests()

    request_records = Request.objects.filter( client_id = Client.objects.get(profile_id =  request.user.id))
    context['request_records'] = request_records

    context['request'] = form
    return render(request, 'base/client.html', context)