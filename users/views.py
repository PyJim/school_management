from django.shortcuts import render, redirect
from django.contrib.auth import login, get_user_model
from django.contrib.auth.views import (LoginView, LogoutView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, TemplateView, View
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
import threading
from .utils import generate_token
from django.contrib import messages





User = get_user_model()


# Create your views here.
class EmailThread(threading.Thread):

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    
    def run(self):
        self.email.send()

def send_activation_email(user, request):
        current_site = get_current_site(request)
        email_subject = 'Activate your account'
        email_body = get_template('registration/activate.html').render({
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': generate_token.make_token(user),
            'activate_url': reverse('activate', kwargs={
                'uidb64': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': generate_token.make_token(user),
            }),
        })

        email = EmailMessage(
            subject=email_subject, 
            body=email_body,
            from_email=settings.EMAIL_HOST_USER,
            to=[user.email],
        )
        email.content_subtype = "html"
        EmailThread(email).start()
        

class UserRegisterView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login') 
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()

        send_activation_email(user, self.request)

        messages.success(self.request, 'A verification email has been sent. Please check your inbox. Remember that it expires in 15 minutes.')

        return super().form_valid(form)


class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'users/profile.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    authentication_form = CustomAuthenticationForm

    def form_valid(self, form):
        user = form.get_user()
        if not user.is_active:
            send_activation_email(user, self.request)
            messages.error(self.request, 'Your account is not activated. Please check your email for the activation link.')
            return render(self.request, self.template_name, {'form': form})

        login(self.request, user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        user = self.request.user
        if user.role == 'teacher':
            return reverse_lazy('teacher_index', kwargs={'username': user.username})
        elif user.role == 'student':
            return reverse_lazy('student_index', kwargs={'username': user.username})
        elif user.role == 'admin':
            return reverse_lazy('administrator_index', kwargs={'username': user.username})
        else:
            return reverse_lazy('profile')


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')


class ActivateAccountView(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        print(token)
        if user is not None and generate_token.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(self.request, 'Account activated successfully')
            return redirect('login')
        else:
            return render(request, 'registration/activation_invalid.html')