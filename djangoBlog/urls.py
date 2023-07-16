from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path

# def homepage(request):
    # return HttpResponse('<h1>Landing Page</h1>')
  
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('landingpage/', homepage),

    path('', include('base.urls')),
]
