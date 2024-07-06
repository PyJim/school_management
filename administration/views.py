from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

# Create your views here.
class AdministratorIndexView(LoginRequiredMixin, TemplateView):
    template_name = 'administrator/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
    
class AdministratorProfileIndexView(LoginRequiredMixin, TemplateView):
    template_name = 'administrator/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
    
class AdministratorSettingsIndexView(LoginRequiredMixin, TemplateView):
    template_name = 'administrator/settings.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
    
class AdministratorCoursesIndexView(LoginRequiredMixin, TemplateView):
    template_name = 'administrator/courses.html'

class AdministratorClassesIndexView(LoginRequiredMixin, TemplateView):
    template_name = 'administrator/classes.html'

class AdministratorGradesIndexView(LoginRequiredMixin, TemplateView):
    template_name = 'administrator/grades.html'

class AdministratorStudentsIndexView(LoginRequiredMixin, TemplateView):
    template_name = 'administrator/students.html'

class AdministratorAdminsIndexView(LoginRequiredMixin, TemplateView):
    template_name = 'administrator/admins.html'

class AdministratorTeachersIndexView(LoginRequiredMixin, TemplateView):
    template_name = 'administrator/teachers.html'

class AdministratorFeesIndexView(LoginRequiredMixin, TemplateView):
    template_name = 'administrator/fees.html'

class AdministratorAttendanceIndexView(LoginRequiredMixin, TemplateView):
    template_name = 'administrator/attendance.html'

class AdministratorAnnouncementsIndexView(LoginRequiredMixin, TemplateView):
    template_name = 'administrator/announcements.html'