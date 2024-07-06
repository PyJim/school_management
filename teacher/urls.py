from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from .views import (TeacherIndexView, TeacherProfileIndexView, TeacherSettingsIndexView, TeacherCoursesIndexView, TeacherClassesIndexView, TeacherGradesIndexView, TeacherStudentsIndexView, TeacherAdminsIndexView, TeacherTeachersIndexView, TeacherFeesIndexView, TeacherAttendanceIndexView, TeacherAnnouncementsIndexView)


urlpatterns = [
    path('<str:username>/', TeacherIndexView.as_view(), name='teacher_index'),
    path('<str:username>/profile', TeacherProfileIndexView.as_view(), name='teacher_profile'),
    path('<str:username>/settings', TeacherSettingsIndexView.as_view(), name='teacher_settings'),
    path('courses', TeacherCoursesIndexView.as_view(), name='teacher_courses'),
    path('classes', TeacherClassesIndexView.as_view(), name='teacher_classes'),
    path('grades', TeacherGradesIndexView.as_view(), name='teacher_grades'),
    path('students', TeacherStudentsIndexView.as_view(), name='teacher_students'),
    path('admins', TeacherAdminsIndexView.as_view(), name='teacher_admins'),
    path('teachers', TeacherTeachersIndexView.as_view(), name='teacher_teachers'),
    path('announcements', TeacherAnnouncementsIndexView.as_view(), name='teacher_announcements'),
    path('attendance', TeacherAttendanceIndexView.as_view(), name='teacher_attendance'),
    path('fees', TeacherFeesIndexView.as_view(), name='teacher_fees'),


]
