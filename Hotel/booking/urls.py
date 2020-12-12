from django.urls import path
from . import views
urlpatterns = [
    path('booking/<str:room>',views.booking,name='booking')
]
