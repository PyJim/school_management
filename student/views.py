from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

# Create your views here.
class StudentIndexView(LoginRequiredMixin, TemplateView):
    template_name = 'student/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
    
class StudentProfileIndexView(LoginRequiredMixin, TemplateView):
    template_name = 'student/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

class StudentSettingsIndexView(LoginRequiredMixin, TemplateView):
    template_name = 'student/settings.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

class StudentCoursesIndexView(LoginRequiredMixin, TemplateView):
    template_name = 'Student/courses.html'

class StudentGradesIndexView(LoginRequiredMixin, TemplateView):
    template_name = 'student/grades.html'

class StudentAdminsIndexView(LoginRequiredMixin, TemplateView):
    template_name = 'student/admins.html'

class StudentTeachersIndexView(LoginRequiredMixin, TemplateView):
    template_name = 'student/teachers.html'

class StudentFeesIndexView(LoginRequiredMixin, TemplateView):
    template_name = 'student/fees.html'

class StudentAttendanceIndexView(LoginRequiredMixin, TemplateView):
    template_name = 'student/attendance.html'

class StudentAnnouncementsIndexView(LoginRequiredMixin, TemplateView):
    template_name = 'student/announcements.html'