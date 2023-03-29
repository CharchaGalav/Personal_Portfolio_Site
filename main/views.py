from django.shortcuts import render
from django.contrib import messages
from django.views import generic
from django.urls import reverse_lazy
from .models import (
    UserProfile, 
    Skill,
    Education,
    Experience,
    Certificate,
    CodingProfiles,
    Project,
    CertificateImages,
    Blog,
    )

from .forms import ContactForm
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache




class IndexView(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_profile'] = UserProfile.objects.first()
        context['skills'] = Skill.objects.all()
        context['educations'] = Education.objects.all()
        context['experiences'] = Experience.objects.all()
        context['certificates'] = Certificate.objects.all()
        context['profiles'] = CodingProfiles.objects.all()
        context['projects'] = Project.objects.all()
        context['certificateImages'] = CertificateImages.objects.all()
        context['blogs'] = Blog.objects.all()
        context['form'] = ContactForm()

        context['num_projects'] = context['projects'].count()
        
        return context
    
    
    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Thank you! Your message has been sent.')
        else:
            messages.add_message(request, messages.ERROR, 'There was an error sending your message. Please try again.')
        return self.get(request, *args, **kwargs)

