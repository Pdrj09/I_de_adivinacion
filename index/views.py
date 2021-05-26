from index.models import eventos, tarotistas
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def index(request):

    #se llaman a la base de datos para sacar la información de -> eventos y tarotistas respectivamente 
    prx_ev = eventos.objects.order_by('fecha')[:5]
    trtsts = tarotistas.objects.order_by('nombre')

    #se carga la plantilla
    doc_template = loader.get_template("index.html")
    #se crea el contexto para pasarlo a la plantilla
    ctx = {
        'prx_ev' : prx_ev,
        'trtsts' : trtsts,
    }
    #se renderiza la plantilla con el contexto
    doc = doc_template.render(ctx)

    #se muestra en la web la plantilla y el contexto renderizados
    return HttpResponse(doc)


def qnsms(request):

    trtsts = tarotistas.objects.order_by('nombre')

    doc_template = loader.get_template("qnsms.html")
    ctx = {
        'trtsts' : trtsts
    }
    doc = doc_template.render(ctx)
    
    return HttpResponse(doc)


