from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.ModelsList.as_view()),
]
