from i_de_adivinacion_web.settings import INSTALLED_APPS
from index.models import eventos, tarotistas
from django.shortcuts import render
from django.http import HttpResponse 
from django.template import loader
import logging



# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create your views here.
def index(request):
    

    user = request.user

    #se carga la plantilla
    doc_template = loader.get_template("index/index.html")
    #se crea el contexto para pasarlo a la plantilla
    ctx = {
        'user' : user
    }
    #se renderiza la plantilla con el contexto
    doc = doc_template.render(ctx)


    if request.user.is_authenticated :
        # Log an error message
        logger.debug('Something went good!')

    #se muestra en la web la plantilla y el contexto renderizados
    return HttpResponse(doc)


def qnsms(request):

    user = request.user.is_authenticated
    trtsts = tarotistas.objects.order_by('nombre')

    doc_template = loader.get_template("index/qnsms.html")
    ctx = {
        'trtsts' : trtsts,
        'user' : user
    }
    doc = doc_template.render(ctx)
    
    return HttpResponse(doc)

def prxev(request):

    user = request.user.is_authenticated
    prx_ev = eventos.objects.order_by('fecha')[:5]

    doc_templare = loader.get_template("index/prx_ev.html")
    ctx = {
        'prx_ev' : prx_ev,
        'user' : user
    }
    doc = doc_templare.render(ctx)

    return HttpResponse(doc)
