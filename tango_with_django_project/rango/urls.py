from django.urls import path
from rango import views
from django.urls import include

app_name = 'rango'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name= 'about'),
    #path('rango/', include('rango.urls')),
    # The above maps any URLs starting with rango/ to be handled by rango
]