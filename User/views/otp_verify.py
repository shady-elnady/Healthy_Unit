from django.http import HttpResponse
from django.shortcuts import render, redirect

from ..models.Profile import Profile

# Create your views here.


def oTP_Verify(request, uid):
    if request.method == "POST":
        profile = Profile.objects.get(uid=uid)
        if request.COOKIES.get("can_otp_enter") != None:
            if profile.otp == request.POST["otp"]:
                red = redirect("home")
                red.set_cookie("verified", True)
                return red
            return HttpResponse("wrong otp")
        return HttpResponse("10 minutes passed")
    return render(request, "Twilio/otp.html", {"id": uid})
