from django.shortcuts import get_object_or_404, render
from django.conf import settings

# from .forms import AddressFrom

# # Create your views here.


# def create(request, username):
#     user = get_object_or_404(User, username=username)
#     form = AddressFrom()
#     if request.method == "POST":
#         form = AddressFrom(request.POST or None)
#         if form.is_valid():
#             form.deploy(user)
#     return render(request, "Maps/maps.html", {"form": form})



def google_map(request):
    key = settings.GOOGLE_API_KEY
    context = {
        'key':key,
    }
    return render(request, 'Maps/google_map.html',context)