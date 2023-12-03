# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login as auth_login, logout, authenticate
# from django.contrib import messages
# from django.contrib.auth.forms import AuthenticationForm
# from django.conf import settings
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.urls import reverse_lazy, reverse
# from allauth.account.views import PasswordChangeView, PasswordSetView

# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.views.generic import ListView
# from django.views.generic.edit import CreateView, UpdateView

# from .models import User
# from .forms import RegistrationForm, SignUpForm


# # Create your views here.


# class RegistrationView(CreateView):
#     template_name = 'registration/register.html'
#     form_class = RegistrationForm

#     def get_context_data(self, *args, **kwargs):
#         context = super(RegistrationView, self).get_context_data(*args, **kwargs)
#         context['next'] = self.request.GET.get('next')
#         return context

#     def get_success_url(self):
#         next_url = self.request.POST.get('next')
#         success_url = reverse('login')
#         if next_url:
#             success_url += '?next={}'.format(next_url)

#         return success_url


# class ProfileView(UpdateView):
#     model = User
#     fields = "__all__"
#     template_name = 'registration/profile.html'

#     def get_success_url(self):
#         return reverse('index')

#     def get_object(self):
#         return self.request.user

# from django.urls import reverse_lazy
# from django.contrib.auth.models import User
# from django.contrib.messages.views import SuccessMessageMixin
# from django.contrib.auth.forms import UserCreationForm

# class Signup(SuccessMessageMixin, CreateView):
#     form = UserCreationForm
#     fields = '__all__'
#     model = User
#     template_name = 'registration/signup.html'
#     # success_url = reverse_lazy('glazes:home page')


# def signUp(req):
#     if req.method == "POST":
#         form = SignUpForm(req.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data["username"]
#             password = form.cleaned_data["password1"]
#             user = authenticate(username=username, password=password)
#             auth_login(req, user)
#             return redirect(settings.LOGIN_REDIRECT_URL)

#     else:
#         form = SignUpForm()

#     context = {
#         "form": form,
#     }

#     return render(req, "registration/signUp.html", context=context)



# def register_request(request):
# 	if request.method == "POST":
# 		form = NewUserForm(request.POST)
# 		if form.is_valid():
# 			user = form.save()
# 			login(request, user)
# 			messages.success(request, "Registration successful." )
# 			return redirect(reverse_lazy('Restaurant:Intro'))
# 		messages.error(request, "Unsuccessful registration. Invalid information.")
# 	form = NewUserForm()
# 	return render (request=request, template_name="Log/sign_up.html", context={"form":form})

# ### Twilio
# # https://www.twilio.com/blog/enable-multiple-otp-methods-django

# def register(request):
#     if request.method=="POST":
#         if User.objects.filter(username__iexact=request.POST['username']).exists():
#             return HttpResponse("User already exists")
#         if User.objects.filter(email__iexact=request.POST['email']).exists():
#             return HttpResponse("User already exists")
#         otp=random.randint(1000,9999)
#         user=User.objects.create_user(
#             username=request.POST['username'],
#             email=request.POST['email'],
#             password=request.POST['password'],
#             mobile=request.POST['mobile'],
#             otp=f'{otp}'
#         )
#         if request.POST['methodOtp']=="methodOtpWhatsapp":
#             messagehandler=TwilioMessageHandler(request.POST['mobile'],otp).send_otp_via_whatsapp()
#         else:
#             messagehandler=TwilioMessageHandler(request.POST['mobile'],otp).send_otp_via_message()
#         return redirect(reverse_lazy('Restaurant:Intro')).set_cookie("can_otp_enter",True,max_age=600)
          
#     return render(request, 'Log/sign_up.html')


# def otpVerify(request,uid):
#     if request.method=="POST":
#         profile=Profile.objects.get(uid=uid)     
#         if request.COOKIES.get('can_otp_enter')!=None:
#             if(profile.otp==request.POST['otp']):
#                 red=redirect("home")
#                 red.set_cookie('verified',True)
#                 return red
#             return HttpResponse("wrong otp")
#         return HttpResponse("10 minutes passed")        
#     return render(request,"Twilio/otp.html",{'id':uid})


# def home(request):
#     if request.COOKIES.get('verified') and request.COOKIES.get('verified')!=None:
#         return HttpResponse(" verified.")
#     else:
#         return HttpResponse(" Not verified.")


from django.conf import settings
from django.contrib.auth.views import LoginView
from django.urls import translate_url
from django.utils.translation import activate, LANGUAGE_SESSION_KEY

# available languages should be obtained from settings.LANGUAGES
available_languages = [lang_code for (lang_code, lang_name) in settings.LANGUAGES]

class CustomLoginView(LoginView):
    def get_success_url(self):
        url = super(CustomLoginView, self).get_success_url()
        user = self.request.user
        if user.is_authenticated():
            language = user.get_setting('language')

            if language in available_languages:
                url = translate_url(url, language)
                activate(language)
                if hasattr(self.request, 'session'):
                    self.request.session[LANGUAGE_SESSION_KEY] = language

        return url