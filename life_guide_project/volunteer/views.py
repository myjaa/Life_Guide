from django.shortcuts import render

def volunteer(request):
    return render(request, 'volunteer/volunteer.html')
