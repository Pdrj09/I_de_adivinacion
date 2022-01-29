from django.forms.forms import Form
from index.models import eventos, tarotistas
from django.shortcuts import redirect, render
from django.http import HttpResponse 
from django.template import loader
from .forms import SignoZodiaco, UserCreationFormWithEmail
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

    doc_template = loader.get_template("index/prx_ev.html")
    ctx = {
        'prx_ev' : prx_ev,
        'user' : user
    }
    doc = doc_template.render(ctx)

    aut(request, user, doc)

    return HttpResponse(doc)


"""This view create the registration form an then redirect the user to the 
    sign form"""
def register(request):
    #create the contex
    ctx = {
        'form' : UserCreationFormWithEmail()
    }

    if request.method == 'POST':
        form = UserCreationFormWithEmail(data=request.POST)
        

        if form.is_valid():
            form.save()
            user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password1"])
            login(request, user)
            return redirect(to='/signo')
            
    #render of the page whit the request, the html page and the contex
    return render(request, 'registration/registro.html', ctx)

""" this view creates the form page of the sign and then redirects to the menu """
def registro_signo(request):
    #create the contex
    ctx = {
        'form' : SignoZodiaco(),
    }

    #if the form is post
    if request.method == 'POST':

        #save the form
        form = SignoZodiaco(request.POST)

        #the form is validated
        if form.is_valid():

            #create the f_form (final form)
            f_form = form.save(False) 
            print(form)
            #add the user id to the form
            f_form.User_id = request.user.id
            print(f_form)
            #save an send the form
            f_form.save() 

            #messages.success(request, "registrado correctamente")# for the future
            #redirect the page to the menu
            return redirect(to='/')
            


    #se renderiza la plantilla con el contexto y con el request
    return render(request, 'registration/registro_signo.html', ctx)

def usr(request):

    user = request.user
    usrn = user.username

    #load the template
    doc_template = loader.get_template("registration/user_menu.html")
    #create the context to the template
    ctx = {
        'user' : user,
        'usrn' : usrn
    }
    #render the template with the context
    doc = doc_template.render(ctx)
    
    aut(request, user, doc)

    #shown the render of the template
    return HttpResponse(doc)


