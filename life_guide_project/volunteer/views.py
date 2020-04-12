from django.shortcuts import render
from math import ceil
from .models import Volunteer

def volunteer(request):
	

	if request.method == "POST":
		first_name= request.POST.get('first_name','')
		last_name= request.POST.get('last_name','')
		phone= request.POST.get('phone','')		
		email= request.POST.get('email','')	
		location = request.POST.get('location','')		
		vol=Volunteer(first_name=first_name, last_name=last_name, phone=phone, email=email, location=location)
		vol.save()
		done = True
		return render(request, 'volunteer/volunteer.html', {'done':done})
	return render(request, 'volunteer/volunteer.html',)
