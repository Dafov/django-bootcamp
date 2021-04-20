from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render

# Create your views here.
from .forms import LoginForm


def login_view(request):
    form = LoginForm(request.post or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(request, username=username, password=password)
        if user != None:
            # user is valid and is_active
            login(request, user)
            return redirecet("/")
        else:
            # attempt = request.session.get("attempt") or 0
            # request.session['attempt'] = attempt + 1
            # return redirect("/invalid-passwod")
            request.session['invalid_user'] = 1  # 1 == True
    return render(request, "forms.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirected("/login")
