from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

import users.models
from users.forms import CustomUserCreationForm, ProfileForm, CustomUserChangeForm
from users.models import CustomUser


# Create your views here.

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"


def login(request):
    return render(request, 'login.html')


def index(request):
    return render(request, 'index.html')


def update_profile(request, user_id):
    # this is used in the template
    if request.method == "POST":
        # user_form = CustomUserChangeForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, "Profile has been updated!")
            return redirect('/')
        else:
            messages.error(request, "Correct the errors in the form")
    else:
        # user_form = CustomUserChangeForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'update_profile.html', {
        'profile_form': profile_form
    })
