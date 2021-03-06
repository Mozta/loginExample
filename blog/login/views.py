from django.shortcuts import render

# Create your views here.
#views.py
from login.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext

from .models import Lista
from .forms import ListaF
from .forms import ModifyF

@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })

    return render_to_response(
    'registration/register.html',
    variables,
    )

def register_success(request):
    return render_to_response(
    'registration/success.html',
    )

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

def modify(request):
    if request.method == 'POST':
        form = ModifyF(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/home/')
    else:
        form = ModifyF()
        #print form
    print request
    variables = RequestContext(request, {
    'form': form
    })

    return render_to_response(
    'modify.html',
    variables,
    )

@login_required
def home(request):
    nombre = request.user.last_name + " " + request.user.first_name
    #latest_list = Lista.objects.order_by('-matricula')[:5]
    latest_list = Lista.objects.filter(tutor=nombre)

    obj = Lista.objects.filter(id=1)#.update(avance=55.3)
    #print "afuera"
    #print request

        #print "es GET"
    form = ListaF()
        #form = latest_list
        #print form.is_bound
        #print form
        #f = CommentForm(initial={'name': 'instance'}, auto_id=False)
    variables = RequestContext(request, {
    'user': request.user, 'latest_list': latest_list, 'form': form
    })

    return render_to_response(
    'home.html',
    variables,
    )
