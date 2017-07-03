import os
import time

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import EmailMessage

from django.template.loader import render_to_string
from django.views.generic import ListView
from weasyprint import HTML
import zipfile

from ContactProject.celery import app
from contactus.models import ContactModel


class ContactsListView(LoginRequiredMixin, ListView):
    model = ContactModel
    template_name = 'contact_list.html'
    context_object_name = 'contacts'


@app.task
def export_contact_to_pdf(request):
    contacts = ContactModel.objects.all()
    for contact in contacts:
        html_string = render_to_string('contact_pdf_template.html', {'contacts': contact})

        html = HTML(string=html_string)
        pdf_file_name = "Exports/%d-%s.pdf" %(int(time.time()), contact.name)
        html.write_pdf(target=pdf_file_name)

    zipf = zipfile.ZipFile('Exports.zip', 'w', zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk("Exports"):
        for file in files:
            zipf.write(os.path.join(root, file))

    html_content = "New pdf exports of existing contacts"
    email = EmailMessage("my subject", html_content, "pdf-contacts-export@admin.com", ["admin@admin.com"])
    email.content_subtype = "html"

    fd = open('manage.py', 'r')
    email.attach('manage.py', fd.read(), 'text/plain')

    res = email.send()

