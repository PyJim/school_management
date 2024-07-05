from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from .views import (UserRegisterView, ActivateAccountView, UserProfileView, CustomLoginView, TeacherIndexView, StudentIndexView, AdministratorIndexView, CustomLogoutView)


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('activate/<uidb64>/<token>/', ActivateAccountView.as_view(), name='activate'),
    path('email-verification-sent/', TemplateView.as_view(template_name="registration/email_verification_sent.html"), name='email_verification_sent'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('teacher/<str:username>/', TeacherIndexView.as_view(), name='teacher_index'),
    path('student/<str:username>/', StudentIndexView.as_view(), name='student_index'),
    path('administrator/<str:username>/', AdministratorIndexView.as_view(), name='administrator_index'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change_form.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
]
