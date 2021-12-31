from django.shortcuts import render,redirect;
from cmsadmin.models import Clint
from cmsadmin.models import Managers
from cmsadmin.models import Alogin
from cmsadmin.models import Hr
from django.http import HttpResponse
def index(request):
		return render(request,"guest/index.html")
def hrlogin(request):
	if request.method=="POST":
		obj = Hr.objects.filter(email=request.POST["txtemail"],password=request.POST["txtpass"])
		if obj.count()>0:
		   s="successfully login"
		   return redirect('/hr')
		else:
		   s="Invalid userid and password"
		   return render(request,"guest/hrlogin.html",{"res":s})

	return render(request,"guest/hrlogin.html")

def clintlogin(request):
	if request.method=="POST":
		obj = Clint.objects.filter(email=request.POST["txtemail"],password=request.POST["txtpass"])
		if obj.count()>0:
		   s="successfully login"
		   return redirect('/clint')
		else:
		   s="Invalid userid and password"
		   return render(request,"guest/clintlogin.html",{"res":s})
	return render(request,"guest/clintlogin.html")

def adminlogin(request):
	if request.method=="POST":
		obj = Alogin.objects.filter(email=request.POST["txtemail"],password=request.POST["txtpass"])
		if obj.count()>0:
		   s="successfully login"
		   return redirect('/cmsadmin')
		else:
		   s="Invalid userid and password"
		   return render(request,"guest/adminlogin.html",{"res":s})
	return render(request,"guest/adminlogin.html")
	
def managerlogin(request):
	if request.method=="POST":
		obj = Managers.objects.filter(email=request.POST["txtemail"],password=request.POST["txtpass"])
		if obj.count()>0:
		   s="successfully login"
		   return redirect('/manager')
		else:
		   s="Invalid userid and password"
		   return render(request,"guest/managerlogin.html",{"res":s})
	return render(request,"guest/managerlogin.html")
def devloperlogin(request):

	return render(request,"guest/devloperlogin.html")