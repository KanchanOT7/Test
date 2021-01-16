from django.http import HttpResponse
from django.shortcuts import redirect, render

from quiz.models import *

def homepage(request):
	if request.method == "GET":
		#all_users = Person.objects.all()
		#for u in all_users:
			#print(u.first_name, u.last_name)
		# kumar_persons = Person.objects.get(last_name='kumar') get() function returns only 1 object
		p = Person.objects.all()[0]
		return render(request, "home.html", {"person": p})
	elif request.method == "POST":
		if 'first' in request.POST and 'last' in request.POST:
			p = Person(first_name=request.POST['first'], last_name=request.POST['last'])
			p.save()
			return HttpResponse("hello")
