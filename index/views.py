from django.forms.forms import Form
from index.models import eventos, tarotistas
from django.shortcuts import redirect, render
from django.http import HttpResponse 
from django.template import loader
from .forms import MyUserCreationForm, SignoZodiaco
from django.contrib.auth import authenticate, login
from django.contrib import messages
from i_de_adivinacion_web import settings
from .models import Perfil
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


def aut(request, user, doc):
    if request.user.is_authenticated :
            # Log an error message
            logger.info('USER -> Ok')
    else:
            logger.info('USER -> NO LOGADO')

    if doc :
            logger.info('plantilla/contexto -> Ok')



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
    
    aut(request, user, doc)

    #se muestra en la web la plantilla y el contexto renderizados
    return HttpResponse(doc)

    

def qnsms(request):

    user = request.user
    trtsts = tarotistas.objects.order_by('nombre')

    doc_template = loader.get_template("index/qnsms.html")
    ctx = {
        'trtsts' : trtsts,
        'user' : user
    }
    doc = doc_template.render(ctx)

    aut(request, user, doc)
    
    return HttpResponse(doc)

def prxev(request):

    user = request.user
    prx_ev = eventos.objects.order_by('fecha')[:5]

    doc_templare = loader.get_template("index/prx_ev.html")
    ctx = {
        'prx_ev' : prx_ev,
        'user' : user
    }
    doc = doc_templare.render(ctx)

    aut(request, user, doc)

    return HttpResponse(doc)

def register(request):
    doc_template = loader.get_template("registration/registro.html")
    #se crea el contexto para pasarlo a la plantilla
    ctx = {
        'form' : MyUserCreationForm(),
        'form_2' : SignoZodiaco()
    }
    if request.method == 'POST':
        formuario = MyUserCreationForm(data=request.POST)
        
        if formuario.is_valid():
            formuario.save()
            user = authenticate(username=formuario.cleaned_data["username"], password=formuario.cleaned_data["password1"])
            login(request, user)
            return redirect(to='/signo')
        #data["form"] = formuario
    #se renderiza la plantilla con el contexto
    
    return render(request, 'registration/registro.html', ctx)
#rec = int(request.POST.get('User'))

def registro_signo(request):
    doc_template = loader.get_template("registration/registro.html")
    #se crea el contexto para pasarlo a la plantilla
    user = request.user
    o = 0
    ctx = {
        'user' : user,
        'form' : SignoZodiaco(),
        'o' : o,
    }
    O = {
        
        'User' : request.user.id,
    }
    if request.method == 'POST':
        formulario = SignoZodiaco(request.POST)

        if formulario.is_valid():
            question = formulario.save(False) 
            question.User_id = request.user.id
            question.save() 
            #formulario.save()
            #messages.success(request, "registrado correctamente")
            return redirect(to='/')

                    #data["form"] = formuario
    #se renderiza la plantilla con el contexto
    
    return render(request, 'registration/registro_signo.html', ctx)