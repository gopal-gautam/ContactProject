from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView, DeleteView, DetailView

from contactus.forms import ContactUsForm
from contactus.models import ContactModel


class ContactUsCreateView(SuccessMessageMixin, CreateView):
    model = ContactModel
    form_class = ContactUsForm
    template_name = 'contactus_form.html'
    success_message = "Thank you for you valueable time"
    success_url = reverse_lazy('thank-you')

class ContactUsUpdateView(UpdateView):
    model = ContactModel
    form_class = ContactUsForm
    template_name = 'contactus_form.html'

class ContactUsThankYouTemplateView(TemplateView):
    template_name = 'contactus_thankyou.html'


class ContactUsDetailView(DetailView):
    model = ContactModel
    template_name = 'view-contact.html'
    context_object_name = 'contact'


class ContactUsDeleteView(DeleteView):
    model = ContactModel
    template_name = 'contactmodel_confirm_delete.html'
    success_url = reverse_lazy('contact_admin:list-contacts')