from django.shortcuts import render

from django.views.generic import ListView
from .models import Member, Career, Contact

from django.views import View

from django.views.generic import TemplateView

class MainView(ListView):
    model = Member
    template_name = 'main/main.html'

class AboutMeView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        context['member'] = Member.objects.get(pk=request.GET['pk'])
        context['careers'] = Career.objects.filter(pk=request.GET['pk'])
        context['contacts'] = Contact.objects.filter(pk=request.GET['pk'])

        return render(request, 'about_me/about_me.html', context)
    
class SkillView(TemplateView):
    template_name = 'skill/skill.html'