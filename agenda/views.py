from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def agenda(request):
    template = loader.get_template('agenda.html')
    return HttpResponse(template.render())

def register(request):
    template = loader.get_template('cadastrar.html')
    return HttpResponse(template.render())

def show_animals(request):
    template = loader.get_template('animais_cadastrados.html')
    return HttpResponse(template.render())

def main(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())