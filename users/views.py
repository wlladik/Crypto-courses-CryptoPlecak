from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegForm, ProfileImageForm, UserUpdaterForm
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == "POST":
        form = UserRegForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}!')
            return redirect('home')
    else:
        form = UserRegForm()

    return render(
        request,
        'users/registration.html',
        {
            'title': 'Registration',
            'form': form
        }
    )


def custom_logout(request):
    logout(request)
    messages.success(request, 'Now you logged out, sign in to your account')
    return redirect("home")


@login_required
def profile(request):
    if request.method == "POST":
        profile_form = ProfileImageForm(request.POST, request.FILES, instance=request.user.profile)
        update_user_form = UserUpdaterForm(request.POST, instance=request.user)

        if profile_form.is_valid() and update_user_form.is_valid():
            update_user_form.save()
            profile_form.save()
            messages.success(request, 'Your account successfully updated')
            return redirect("profile")

    else:
        profile_form = ProfileImageForm(instance=request.user.profile)
        update_user_form = UserUpdaterForm(instance=request.user)

    data = {
        'profileForm': profile_form,
        'updateForm': update_user_form
    }

    return render(request, "users/profile.html", data)
