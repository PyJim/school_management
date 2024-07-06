from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from .views import (AdministratorIndexView, AdministratorProfileIndexView, AdministratorSettingsIndexView,
                    AdministratorCoursesIndexView, AdministratorClassesIndexView, AdministratorGradesIndexView, AdministratorStudentsIndexView, AdministratorAdminsIndexView, AdministratorTeachersIndexView, AdministratorFeesIndexView, AdministratorAttendanceIndexView, AdministratorAnnouncementsIndexView)


urlpatterns = [
    path('<str:username>/', AdministratorIndexView.as_view(), name='administrator_index'),
    path('<str:username>/profile', AdministratorProfileIndexView.as_view(), name='administrator_profile'),
    path('<str:username>/settings', AdministratorSettingsIndexView.as_view(), name='administrator_settings'),
    path('courses', AdministratorCoursesIndexView.as_view(), name='administrator_courses'),
    path('classes', AdministratorClassesIndexView.as_view(), name='administrator_classes'),
    path('grades', AdministratorGradesIndexView.as_view(), name='administrator_grades'),
    path('students', AdministratorStudentsIndexView.as_view(), name='administrator_students'),
    path('admins', AdministratorAdminsIndexView.as_view(), name='administrator_admins'),
    path('teachers', AdministratorTeachersIndexView.as_view(), name='administrator_teachers'),
    path('announcements', AdministratorAnnouncementsIndexView.as_view(), name='administrator_announcements'),
    path('attendance', AdministratorAttendanceIndexView.as_view(), name='administrator_attendance'),
    path('fees', AdministratorFeesIndexView.as_view(), name='administrator_fees'),
    
]
