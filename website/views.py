
from django.shortcuts import render, reverse
from django.views.generic import View,TemplateView,CreateView
from .models import Contact
from django.core.mail import send_mail

class Home(TemplateView):
    template_name='website/home.html'

class Contact(CreateView):
    model = Contact
    fields = ('__all__')
    def get_success_url(self):
        # send_mail(
        #     "Subject here",
        #     "Here is the message.",
        #     "vincent.berry11@gmail.com",
        #     ["bodecroofing@embarqmail.com"],
        #     fail_silently=False,
        # )
        return reverse('contact')

class Services(TemplateView):
    template_name='website/services.html'

class Gallery(TemplateView):
    template_name='website/gallery.html'

class About(TemplateView):
    template_name='website/about.html'