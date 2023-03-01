from django.shortcuts import render
from .models import AllModels

# Create your views here.
from django.views import View
from django.views.generic import ListView


# def test(request):
#     return render(request, 'main_page/index.html')


class ModelsList(ListView):
    model = AllModels
    template_name = 'main_page/index.html'
    context_object_name = 'models'
