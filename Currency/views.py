from django.shortcuts import render
from django.utils.translation import get_language_from_request

# Create your views here.


def home(request):
    language = get_language_from_request(request)
    return render(request=request,)