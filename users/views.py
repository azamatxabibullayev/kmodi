from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.utils.translation import gettext as _
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, ProfileUpdateForm


def register_student(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'student'
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form, 'title': _('Register')})


def login_view(request):
    if request.method == "POST":
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        user = authenticate(request, phone=phone, password=password)
        if user is not None:
            login(request, user)
            if user.role == 'admin':
                return redirect('dashboard:home')
            else:
                return redirect('home')
        else:
            return render(request, 'users/login.html', {'error': _('Invalid phone number or password')})
    return render(request, 'users/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def profile_view(request):
    return render(request, 'users/profile.html')


@login_required
def profile_update_view(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, 'users/profile_update.html', {'form': form})
