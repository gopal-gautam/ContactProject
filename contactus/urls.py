from django.conf.urls import url, include

from contactus import views

urlpatterns = [

    url(r'^$', views.ContactUsCreateView.as_view(), name="contact-us"),
    url(r'^thankyou/$', views.ContactUsThankYouTemplateView.as_view(), name="thank-you"),
    url(r'^contact-view/(?P<pk>\d+)/$', views.ContactUsDetailView.as_view(), name="view-contact"),
    url(r'^contact-update/(?P<pk>\d+)/$', views.ContactUsUpdateView.as_view(), name="update-contact"),
    url(r'^contact-delete/(?P<pk>\d+)/$', views.ContactUsDeleteView.as_view(), name="delete-contact"),

]