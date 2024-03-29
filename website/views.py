from django.views.generic import View,TemplateView
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm

class Home(TemplateView):
    template_name='website/home.html'

class Contact(View):
    def get(self,request):
        if request.method == "GET":
            context = {
                'form': ContactForm()
            }
            return render(request,'website/contact_form.html', context=context)
    def post(self,request):
        if request.method == "POST":
            contact_dict = request.POST.dict()
            send_mail(
                "New Bo-Dec Lead...",
                f" Name: {contact_dict.get('name')} \n Company: {contact_dict.get('company')} \n Email: {contact_dict.get('email')} \n Phone: {contact_dict.get('phone_0')} \n Phone Ext.: {contact_dict.get('phone_1')} \n Message: {contact_dict.get('message')}",
                "vincent.berry11@gmail.com",
                ["bodecroofing@embarqmail.com","vincent.berry11@gmail.com"],
                fail_silently=False,
            )
            return redirect('contact')

class Services(TemplateView):
    template_name='website/services.html'

class Gallery(TemplateView):
    template_name='website/gallery.html'

class About(TemplateView):
    template_name='website/about.html'