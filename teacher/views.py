from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

# Create your views here.
class TeacherIndexView(LoginRequiredMixin, TemplateView):
    template_name = 'teacher/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
    
class TeacherProfileIndexView(LoginRequiredMixin, TemplateView):
    template_name = 'teacher/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
    
class TeacherSettingsIndexView(LoginRequiredMixin, TemplateView):
    template_name = 'teacher/settings.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
    
class TeacherCoursesIndexView(LoginRequiredMixin, TemplateView):
    template_name = 'teacher/courses.html'

class TeacherClassesIndexView(LoginRequiredMixin, TemplateView):
    template_name = 'teacher/classes.html'

class TeacherGradesIndexView(LoginRequiredMixin, TemplateView):
    template_name = 'teacher/grades.html'

class TeacherStudentsIndexView(LoginRequiredMixin, TemplateView):
    template_name = 'teacher/students.html'

class TeacherAdminsIndexView(LoginRequiredMixin, TemplateView):
    template_name = 'teacher/admins.html'

class TeacherTeachersIndexView(LoginRequiredMixin, TemplateView):
    template_name = 'teacher/teachers.html'

class TeacherFeesIndexView(LoginRequiredMixin, TemplateView):
    template_name = 'teacher/fees.html'

class TeacherAttendanceIndexView(LoginRequiredMixin, TemplateView):
    template_name = 'teacher/attendance.html'

class TeacherAnnouncementsIndexView(LoginRequiredMixin, TemplateView):
    template_name = 'teacher/announcements.html'