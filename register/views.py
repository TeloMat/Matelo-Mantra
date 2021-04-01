from django.shortcuts import render, redirect
from .forms import RegisterForm


# Create your views here.


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect("/login")
        return redirect("/register")
    else:
        form = RegisterForm()
    return render(response, "register/signup.html", {"form":form})


def signin(response):
    if response.user.is_authenticated:
        return redirect("/signin")
    return redirect("/home")
