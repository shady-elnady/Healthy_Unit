from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy


def logIn(request):
    # if request.method == "POST":
    #     profile = Profile.objects.get(uid=uid)
    #     if request.COOKIES.get("can_otp_enter") != None:
    #         if profile.otp == request.POST["otp"]:
    #             red = redirect("home")
    #             red.set_cookie("verified", True)
    #             return red
    #         return HttpResponse("wrong otp")
    #     return HttpResponse("10 minutes passed")
    return render(request, "Log/logIn.html")
