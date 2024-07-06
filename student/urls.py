from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from .views import (StudentIndexView, StudentProfileIndexView, StudentSettingsIndexView, StudentCoursesIndexView, StudentGradesIndexView, StudentAdminsIndexView, StudentTeachersIndexView, StudentFeesIndexView, StudentAttendanceIndexView, StudentAnnouncementsIndexView)


urlpatterns = [
    path('<str:username>/', StudentIndexView.as_view(), name='student_index'),
    path('<str:username>/profile', StudentProfileIndexView.as_view(), name='student_profile'),
    path('<str:username>/settings', StudentSettingsIndexView.as_view(), name='student_settings'),
    path('courses', StudentCoursesIndexView.as_view(), name='student_courses'),
    path('grades', StudentGradesIndexView.as_view(), name='student_grades'),
    path('admins', StudentAdminsIndexView.as_view(), name='student_admins'),
    path('teachers', StudentTeachersIndexView.as_view(), name='student_teachers'),
    path('announcements', StudentAnnouncementsIndexView.as_view(), name='student_announcements'),
    path('attendance', StudentAttendanceIndexView.as_view(), name='student_attendance'),
    path('fees', StudentFeesIndexView.as_view(), name='student_fees'),

]
