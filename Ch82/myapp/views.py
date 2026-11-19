
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import FormView
from myapp.forms import ContactForm
from myapp.models import Contact


# Create your views here.
class ContactFormView(FormView):
    template_name = 'myapp/contact.html'
    form_class = ContactForm
    success_url = '/thanks/'
    initial = {'name':"umar", 'email':'umar@example.com'}
    
    def form_valid(self, form):
        print(form)
        print(form.cleaned_data['name'])
        print(form.cleaned_data['email'])
        print(form.cleaned_data['msg'])
        # save the checked data as a new row in the Contact table
        Contact.objects.create(
            name=form.cleaned_data['name'],
            email=form.cleaned_data['email'],
            msg=form.cleaned_data['msg'],
        )
        return super().form_valid(form)
        # return HttpResponse("thankyou form submitted")
        
    def form_invalid(self, form):
        messages.error(
            self.request, 'there was an error with your form submission'
        )
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["extra"] =  "hello form"
        return context
    
        