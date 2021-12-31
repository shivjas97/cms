from django.db.models.manager import Manager
from django.shortcuts import redirect, render
from cmsadmin.models import Clint
from cmsadmin.models import Managers
from cmsadmin.models import Devlopers
from django.http import HttpResponse

def index(request):
	
		return render(request,"hr/index.html")
def addemployee(request):
	if request.method=="POST":
		chkemail= Devlopers.objects.filter(email=request.POST["txtemail"])
		if chkemail.count()>0:
			return HttpResponse("Emailid already exist")
	
		else:
			obj = Devlopers(name=request.POST["txtname"],email=request.POST["txtemail"],mobile=request.POST["txtnumber"],
			password=request.POST["txtpass"],knowledge=request.POST["txtknow"],designation =request.POST["txtdesig"],
			education=request.POST["txtedu"],exp=request.POST["txtexp"],salary=request.POST["txtsal"],location=request.POST["txtlocation"],
			gender=request.POST["txtgender"],age=request.POST["txtage"],about=request.POST["txtabt"])
			obj.save()
			return render(request,"hr/addemployee.html",{'res':'Registration Successfull'})
	return render(request,"hr/addemployee.html")

def viewdevloper(request):
		r = Devlopers.objects.all() #select * from Devlopers
		return render(request,"hr/viewdevloper.html",{"res":r})
def devloperprofile(request):
		r = Devlopers.objects.filter(pk=request.GET["q"]) #select id from Devlopers
		return render(request,"hr/devloperprofile.html",{"res":r})
def editdevloper(request):
		if request.method=="POST":
			rec = Devlopers.objects.get(pk=request.POST["txtid"])
			rec.name = request.POST["txtname"]
			rec.email = request.POST["txtemail"]
			rec.mobile = request.POST["txtnumber"]
			rec.password = request.POST["txtpass"]
			rec.gender = request.POST["txtgender"]
			rec.age = request.POST["txtage"]
			rec.location = request.POST["txtlocation"]
			rec.education = request.POST["txtedu"]
			rec.knowledge = request.POST["txtknow"]
			rec.designation = request.POST["txtdesig"]
			rec.exp = request.POST["txtexp"]
			rec.salary = request.POST["txtsal"]
			rec.about = request.POST["txtabt"]
			rec.save()
			return redirect("viewdevloper")
		else:
			obj= Devlopers.objects.get(pk=request.GET["q"])
			return render(request,"hr/editdevloper.html",{"res":obj})
def deletedevloper(request):
		obj = Devlopers.objects.get(pk=request.GET["q"]).delete()
		return redirect("viewdevloper")

def viewmanager(request):
		r = Managers.objects.all() #select * from Managers
		return render(request,"hr/viewmanager.html",{"res":r})
def addmanager(request):
	if request.method=="POST":
		chkemail= Managers.objects.filter(email=request.POST["txtemail"])
		if chkemail.count()>0:
			return HttpResponse("Emailid already exist")
		else:
			obj = Managers(name=request.POST["txtname"],email=request.POST["txtemail"],mobile=request.POST["txtnumber"],
			password=request.POST["txtpass"],knowledge=request.POST["txtknow"],
			education=request.POST["txtedu"],exp=request.POST["txtexp"],salary=request.POST["txtsal"],location=request.POST["txtlocation"],
			gender=request.POST["txtgender"],age=request.POST["txtage"],about=request.POST["txtabt"])
			obj.save()
			return render(request,"hr/addmanager.html",{'res':'Registration Successfull'})
	return render(request,"hr/addmanager.html")

def managerprofile(request):
		r = Managers.objects.filter(pk=request.GET["q"]) #select id from Managers
		return render(request,"hr/managerprofile.html",{"res":r})

def deletemanager(request):
		obj = Managers.objects.get(pk=request.GET["q"]).delete()
		return redirect("viewmanager")

def editmanager(request):
		if request.method=="POST":
			rec = Managers.objects.get(pk=request.POST["txtid"])
			rec.name = request.POST["txtname"]
			rec.email = request.POST["txtemail"]
			rec.mobile = request.POST["txtnumber"]
			rec.password = request.POST["txtpass"]
			rec.gender = request.POST["txtgender"]
			rec.age = request.POST["txtage"]
			rec.location = request.POST["txtlocation"]
			rec.education = request.POST["txtedu"]
			rec.knowledge = request.POST["txtknow"]
			rec.exp = request.POST["txtexp"]
			rec.salary = request.POST["txtsal"]
			rec.about = request.POST["txtabt"]
			rec.save()
			return redirect("viewmanager")
		else:
			obj= Managers.objects.get(pk=request.GET["q"])
			return render(request,"hr/editmanager.html",{"res":obj})

def viewclints(request):
		r1 = Clint.objects.all() #select * from clints
		return render(request,"hr/viewclints.html",{"res1":r1})
def addclint(request):
	if request.method=="POST":
		chkemail= Clint.objects.filter(email=request.POST["txtemail"])
		if chkemail.count()>0:
			return HttpResponse("Emailid already exist")
		else:
			obj = Clint(name=request.POST["txtname"],email=request.POST["txtemail"],mobile=request.POST["txtnumber"],password=request.POST["txtpass"],cname=request.POST["txtcom"],pname=request.POST["txtproject"])
			obj.save()
			return render(request,"hr/addclint.html",{'res':'Registration Successfull'})
	return render(request,"hr/addclint.html")

def editclint(request):
	if request.method=="POST":
		rec = Clint.objects.get(pk=request.POST["txtid"])
		rec.name = request.POST["txtname"]
		rec.email = request.POST["txtemail"]
		rec.mobile = request.POST["txtnumber"]
		rec.password = request.POST["txtpass"]
		rec.cname = request.POST["txtcom"]
		rec.pname = request.POST["txtpname"]
		rec.location = request.POST["txtlocation"]
		rec.about = request.POST["txtabt"]
		rec.save()
		return redirect("viewclints")
	else:
		obj= Clint.objects.get(pk=request.GET["q"])
		return render(request,"hr/editclint.html",{"res":obj})

def clintprofile(request):
		r = Clint.objects.filter(pk=request.GET["q"]) #select id from Clint
		return render(request,"hr/clintprofile.html",{"res":r})

def deleteclint(request):
	obj = Clint.objects.get(pk=request.GET["q"]).delete()
	return redirect("/hr/viewclint")