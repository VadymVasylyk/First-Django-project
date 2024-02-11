from django.shortcuts import render, redirect
from .forms import UserRegForm, UserUpdateForm, ProfileUpdateForm, MessageForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib import messages


def register(request):
    if request.method == "POST":
        form = UserRegForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserRegForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == "POST":
        userForm = UserUpdateForm(request.POST, instance=request.user)
        profileForm = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if userForm.is_valid() and profileForm.is_valid():
            userForm.save()
            profileForm.save()
        return redirect('profile')
    else:
        userForm = UserUpdateForm(instance=request.user)
        profileForm = ProfileUpdateForm(instance=request.user.profile)
        data = {
            'userForm': userForm,
            'profileForm': profileForm
        }
        return render(request, 'users/profile.html', data)


def contact(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()

            subject = form.cleaned_data['title']
            plain_message = form.cleaned_data['text']
            from_email = f"From <{form.cleaned_data['sender']}>"
            to = "vasylyk.vadym97@gmail.com"
            send_mail(subject, plain_message, from_email, [to])
            messages.success(request, f'Message sent successfully')

            return redirect('home')
    else:
        form = MessageForm()
    return render(request, "users/contact-us.html", {'form': form})
