from django.shortcuts import render
from django.shortcuts import redirect

def shelter(request):
    response = redirect(
        'https://www.google.com/maps/search/?api=1&query=disaster+shelter')
    return response
