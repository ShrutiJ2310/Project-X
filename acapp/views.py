from django.shortcuts import render
from math import pi, pow

def home(request):
	if request.POST.get("radius"):
		radius = float(request.POST.get("radius"))
		area = pi*pow(radius,2)
		circum = 2*pi*radius
		circum = round(circum,2)
		area = round(area,2)
		msg = "Area = "+str(area)+" Circumference = "+str(circum)
		return render(request,"home.html",{"msg":msg})
	else:
		return render(request,"home.html")
