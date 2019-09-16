from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import News,Tournament,Profile
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import NewUserForm,UserUpdateForm,ProfileUpdateForm


# Create your views here.
def homepage(request):
    return render(request = request,
                  template_name='main/home.html',
                  context = {"news":News.objects.all})
def tournaments(request):
    return render(request=request,
                template_name="main/tournaments.html",
                context = {"tournaments":Tournament.objects.all})
def rankings(request):
    return render(request=request,
                    template_name="main/rankings.html",
                        context = {"profiles":Profile.objects.all})
def gallery(request):
    return render(request=request,
                    template_name="main/gallery.html")
def profile(request):
    return render(request=request,
                template_name="main/profile.html")
def history(request):
    return render(request=request,
                  template_name="main/history.html")
def donate(request):
    return render(request=request,
                 template_name="main/donate.html")
def contact(request):
    return render(request=request,
                    template_name="main/contact.html")
def learn(request):
    return render(request=request,
                  template_name="main/learn.html")
def profile_update(request):
    if request.method=='POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Successfully updated profile")
            return redirect("main:profile")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request=request,
                template_name="main/profile_update.html",context=context)
def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New account created: {username}")
            login(request, user)
            return redirect("main:homepage")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

            return render(request = request,
                          template_name = "main/register.html",
                          context={"form":form})

    form = NewUserForm
    return render(request = request,
                  template_name = "main/register.html",
                  context={"form":form})
def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("main:homepage")
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "main/login.html",
                    context={"form":form})
def play(request):
    return render(request = request,
                  template_name='Go-Game/index.html')