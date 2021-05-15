from i_de_adivinacion_web.settings import TEMPLATES
from django.shortcuts import render
from django.template import Template, Context
from django.http import HttpResponse

# Create your views here.
def index(request):

    doc_externo = open("templates/index.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()
    doc = plt.render(ctx)

    return HttpResponse(doc)