from django.conf.urls import url, include

from contactusadmin import views

urlpatterns = [

    url(r'^$', views.ContactsListView.as_view(), name="list-contacts"),
    url(r'^contacts-export/$', views.export_contact_to_pdf, name="export-contact"),

]