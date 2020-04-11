from django.shortcuts import render

def shelter(request):
    return render(request, 'shelter/shelter.html')
