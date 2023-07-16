from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    # path('home/', views.home, name="home"),
    path('about/', views.about, name="about" ),
    path('blog/', views.blog, name="blog" ),
    path('contact/', views.contact, name="contact" ),
    path('dashboard/', views.dashboard, name="dashboard" ),
]