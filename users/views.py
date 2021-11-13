from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView

from .models import User
from .forms import LoginForm
# Create your views here.

class LoginView(LoginView):
    template_name = 'users/login.html'
    authentication_form = LoginForm
    redirect_authenticated_user = True 
    
class Dashboard(LoginRequiredMixin, TemplateView):
    template_name = 'users/dashboard.html'
    login_url = reverse_lazy('app_users:login')
    
    
class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'users/profile.html'
    context_object_name = 'profile'
    
    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        id = self.kwargs['pk']
        object = User.objects.get(id=id)
        leader = User.objects.get(id_employee=object.leader)
        context['profile'] = object
        context['subalternos'] = User.objects.filter(leader=context['profile'].id_employee)
        context['employee'] = leader
        return context