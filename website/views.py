
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
        contact_dict = self.request.POST.dict()
        print(contact_dict)
        send_mail(
            "New Bo-Dec Lead...",
            f" Name: {contact_dict.get('name')} \n Company: {contact_dict.get('company')} \n Email: {contact_dict.get('email')} \n Phone: {contact_dict.get('phone_0')} \n Ext.: {contact_dict.get('phone_1')} \n Description: {contact_dict.get('description')}",
            "vincent.berry11@gmail.com",
            ["bodecroofing@embarqmail.com"],
            fail_silently=False,
        )
        return reverse('contact')

class Services(TemplateView):
    template_name='website/services.html'

class Gallery(TemplateView):
    template_name='website/gallery.html'

class About(TemplateView):
    template_name='website/about.html'