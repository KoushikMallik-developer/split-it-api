from django.shortcuts import render, redirect

from .login_form import LoginForm
from .registration_form import RegistrationForm, VerifyEmailForm


def user_login(request):
    if request.method == "POST":
        form = LoginForm(**request.POST.dict())
        response_data = form.authenticate(request=request)
        if request.session.get("is_logged_in"):
            return redirect("/")
        else:
            return render(
                request, "users/login.html", context=response_data.model_dump()
            )
    else:
        return render(request, "users/login.html")


def user_logout(request):
    # logout(request)
    return redirect("login")


def user_register(request):
    if request.method == "POST":
        form = RegistrationForm(**request.POST.dict())
        form.username = form.fname.lower()
        response_data = form.register(request)
        if response_data.successMessage:
            return render(
                request,
                "users/email_verification.html",
                context=response_data.model_dump(),
            )
        else:
            return render(
                request, "users/register.html", context=response_data.model_dump()
            )
    else:
        return render(request, "users/register.html")


def user_profile(request):
    if request.method == "GET":
        if request.session.get("is_logged_in") and request.session.get("access_token"):
            # TODO: NEED TO FETCH PROFILE DETAILS
            return render(request, "users/profile.html")
        else:
            return redirect("/login")


def verify_email(request):
    if request.method == "POST":
        form = VerifyEmailForm(
            email=request.session.get("email"), otp=request.POST.get("otp")
        )
        del request.session["email"]
        response_data = form.verify(request)
        if response_data.token:
            request.session["is_logged_in"] = True
            request.session["access_token"] = response_data.token.get("access")
            request.session["refresh_token"] = response_data.token.get("refresh")
            return redirect("/")
        else:
            request.session["is_logged_in"] = False
            return render(
                request,
                "users/email_verification.html",
                context=response_data.model_dump(),
            )
