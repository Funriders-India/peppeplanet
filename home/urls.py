from django.urls import path
from . import views
from .views import get_in_touch

# Create your views here.
urlpatterns = [
    path("", views.index, name="index"),

    path("homeheader", views.homeheader, name="homeheader"),
    path("homefooter", views.homefooter, name="homefooter"),
    path("activities", views.activities, name="activities"),
    path("offers", views.offers, name="offers"),
    path("get_in_touch", views.get_in_touch, name="get_in_touch"),
    path("peppe_party", views.peppe_party, name="peppe_party"),
    path("peppe_cafe", views.peppe_cafe, name="peppe_cafe"),
    path("terms_and_conditions", views.terms_and_conditions, name="terms_and_conditions"), 
    path("faq", views.faq, name="faq"),  
    path("privacy_and_policy", views.privacy_and_policy, name="privacy_and_policy"),    
    path("base", views.base, name="base"),
    path("about", views.about, name="about"), 
    # path("contact", views.contact, name="contact"),
    # path("rides", views.rides, name="rides"),
    # path("enquiry", views.enquiry, name="enquiry"),
    path("franchise", views.franchise, name="franchise"),
    path("news_and_events", views.news_and_events, name="news_and_events"),
    path("careers", views.careers, name="careers"),
    path("little_peppe", views.little_peppe, name="little_peppe"),
    path("peppe_toys", views.peppe_toys, name="peppe_toys"),
    path("packages.", views.packages, name="packages"),
    path("locations.", views.locations, name="locations"),
    path("testimonials", views.testimonials, name="testimonials"),
    path("peppe_style", views.peppe_style, name="peppe_style"),
    path("activities_detail", views.activities_detail, name="activities_detail"),
    path('get_in_touch', views.get_in_touch, name='get_in_touch'),
    path('_send_two_emails_in_background', views._send_two_emails_in_background, name='_send_two_emails_in_background'),
 

   

    
]

