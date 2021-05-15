from i_de_adivinacion_web.settings import TEMPLATES
from django.shortcuts import render
from django.template import Template, Context
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):

    doc_template = loader.get_template("index.html")
    ctx = {}
    doc = doc_template.render(ctx)

    return HttpResponse(doc)