from django.shortcuts import render
from django.views.generic import (
    TemplateView
)

# Create your views here.


class Home(TemplateView):
    # numero_contratos = list(range(1,10))

    template_name = "home/inicio.html"





