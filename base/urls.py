from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard', views.dashboard_view, name='dashboard'),
    path('about', views.about_view, name='about'),
    path('blogs', views.blogs_view, name='blogs'),
    path('feedback', views.feedback_view, name='feedback'),
    path('contact', views.contact_view, name='contact'),
    path('download', views.download_view, name='download'),
    path('terms_conditions', views.terms_conditions_view, name='terms_conditions'),
    path('blog/<str:blog_id>', views.blog_view, name='blog'),
   
]
