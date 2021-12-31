import cmsadmin
from django.shortcuts import redirect, render
from .models import Clint
from .models import Managers
from .models import Hr
from .models import Project  
from .models import Devlopers
from .models import AssignProject
from django.http import HttpResponse
def index(request):
	return render(request,"cmsadmin/index.html")
#------------------------------------------------------------------------------------------manager
def allmanagers(request):
	r = Managers.objects.all() #select * from Managers  (table View)
	return render(request,"cmsadmin/allmanagers.html",{"res":r})

def managemanager(request):
	r = Managers.objects.all() #select * from Managers   (grid View)
	return render(request,"cmsadmin/managemanager.html",{"res":r})

def viewmanager(request):
		r = Managers.objects.filter(pk=request.GET["q"])  #select * from Managers where id = id
		return render(request,"cmsadmin/viewmanager.html",{"res":r})

def edit(request):
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
		return redirect("/cmsadmin/allmanagers")
	else:
		obj= Managers.objects.get(pk=request.GET["q"])
		return render(request,"cmsadmin/edit.html",{"res":obj})

def delete(request):
	obj = Managers.objects.get(pk=request.GET["q"]).delete()
	return redirect("/cmsadmin/allmanagers")
#----------------------------------------------------------------------------------------- HR
def addhr(request):
	if request.method=="POST":
		chkemail= Hr.objects.filter(email=request.POST["txtemail"])
		if chkemail.count()>0:
			return HttpResponse("Emailid already exist")
		else:
			obj = Hr(name=request.POST["txtname"],email=request.POST["txtemail"],mobile=request.POST["txtnumber"],password=request.POST["txtpass"],
			gender=request.POST["txtgender"],age=request.POST["txtage"],education=request.POST["txtknow"],location=request.POST["txtlocation"],
			skills=request.POST["txtskills"],exp=request.POST["txtexp"],salary=request.POST["txtsal"],about=request.POST["txtabt"])
			obj.save()
			return render(request,"cmsadmin/addhr.html",{'res':'Registration Successfull'})
	return render(request,"cmsadmin/addhr.html")

def allhr(request):
	r = Hr.objects.all() #select * from hr
	return render(request,"cmsadmin/allhr.html",{"res":r})


def edithr(request):
	if request.method=="POST":
		rec = Hr.objects.get(pk=request.POST["txtid"])
		rec.name = request.POST["txtname"]
		rec.email = request.POST["txtemail"]
		rec.mobile = request.POST["txtnumber"]
		rec.password = request.POST["txtpass"]
		rec.gender = request.POST["txtgender"]
		rec.age = request.POST["txtage"]
		rec.location = request.POST["txtlocation"]
		rec.education = request.POST["txtknow"]
		rec.skills = request.POST["txtskills"]
		rec.exp = request.POST["txtexp"]
		rec.salary = request.POST["txtsal"]
		rec.about = request.POST["txtabt"]
		rec.save()
		return redirect("/cmsadmin/allhr")
	else:
		obj= Hr.objects.get(pk=request.GET["q"])
		return render(request,"cmsadmin/edithr.html",{"res":obj})

def deletehr(request):
	obj = Hr.objects.get(pk=request.GET["q"]).delete()
	return redirect("/cmsadmin/allhr")

def viewhr(request):
		r = Hr.objects.filter(pk=request.GET["q"])  #select * from hr where id = id
		return render(request,"cmsadmin/viewhr.html",{"res":r})
#-----------------------------------------------------------------------------------------------Clint
def allclint(request):
	r1 = Clint.objects.all() #select * from clints
	return render(request,"cmsadmin/allclint.html",{"res1":r1})

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
		return redirect("/cmsadmin/allclint")
	else:
		obj= Clint.objects.get(pk=request.GET["q"])
		return render(request,"cmsadmin/editclint.html",{"res":obj})

def viewclint(request):
		r = Clint.objects.filter(pk=request.GET["q"])  #select * from clint where id = id
		return render(request,"cmsadmin/viewclint.html",{"res":r})

def deleteclint(request):
	obj = Clint.objects.get(pk=request.GET["q"]).delete()
	return redirect("/cmsadmin/allclint")

#------------------------------------------------------------------------------------------project
def addproject(request):
	r = Clint.objects.all() #select Company Name  from clint
	if request.method=="POST":
		chkname= Project.objects.filter(name=request.POST["txtname"])
		if chkname.count()>0:
			return HttpResponse("Project already exist")
		else:
			obj = Project(name=request.POST["txtname"],desc=request.POST["txtdes"],status=request.POST["txtstatus"],ccom=request.POST["txtcom"],date=request.POST["txtdate"],
			type=request.POST["txttype"],estbudget=request.POST["txtestbudget"],estamt=request.POST["txtestamt"],estdur=request.POST["txtesttime"])
			obj.save()
			return render(request,"cmsadmin/addproject.html",{'res':'Project Added Successfull'})
	return render(request,"cmsadmin/addproject.html",{'res1':r})
	
def allproject(request):
	r = Project.objects.all() #select * from Project
	return render(request,"cmsadmin/allproject.html",{"res":r})

def editproject(request):
	if request.method=="POST":
		rec = Project.objects.get(pk=request.POST["txtid"])
		rec.name = request.POST["txtname"]
		rec.desc = request.POST["txtdes"]
		rec.status = request.POST["txtstatus"]
		#rec.ccom = request.POST["txtcom"]
		rec.date = request.POST["txtdate"]
		rec.type = request.POST["txttype"]
		rec.estbudget = request.POST["txtestbudget"]
		rec.estamt = request.POST["txtestamt"]
		rec.estdur = request.POST["txtesttime"]
		rec.save()
		return redirect("/cmsadmin/allproject")
	else:
		obj= Project.objects.get(pk=request.GET["q"])
		return render(request,"cmsadmin/editproject.html",{"res":obj})

def deleteproject(request):
	obj = Project.objects.get(pk=request.GET["q"]).delete()
	return redirect("/cmsadmin/allproject")

def viewproject(request):
		r = Project.objects.filter(pk=request.GET["q"])  #select * from Project where id = id
		return render(request,"cmsadmin/viewproject.html",{"res":r})

#------------------------------------------------------------------------------------------------Devloper
def alldevloper(request):
	r = Devlopers.objects.all() #select * from devlopers
	return render(request,"cmsadmin/alldevloper.html",{"res":r})

def editdevloper(request):
	if request.method=="POST":
		rec = Devlopers.objects.get(pk=request.POST["txtid"])
		rec.name = request.POST["txtname"]
		rec.email = request.POST["txtemail"]
		rec.mobile = request.POST["txtnumber"]
		rec.password = request.POST["txtpass"]
		rec.cname = request.POST["txtcom"]
		rec.pname = request.POST["txtpname"]
		rec.location = request.POST["txtlocation"]
		rec.about = request.POST["txtabt"]
		rec.save()
		return redirect("/cmsadmin/alldevloper")
	else:
		obj= Devlopers.objects.get(pk=request.GET["q"])
		return render(request,"cmsadmin/editdevloper.html",{"res":obj})

def viewdevloper(request):
		r = Devlopers.objects.filter(pk=request.GET["q"])  #select * from devloper where id = id
		return render(request,"cmsadmin/viewdevloper.html",{"res":r})

def deletedevloper(request):
	obj = Devlopers.objects.get(pk=request.GET["q"]).delete()
	return redirect("/cmsadmin/alldevloper")

#-------------------------------------------------------------------------------------assignproject
def assignproject(request):
	if request.method=="POST":#select Company Name  from clint
		rec = AssignProject(projectid=request.POST["txtpid"],managerid=request.POST["txtmid"],date=request.POST["txtdate"])
		rec.save()
		return redirect("/cmsadmin/assignproject")
	else:
		r = Project.objects.filter(pk=request.GET["q"])  #select * from Project where id = id
		r1 = Managers.objects.all()
		return render(request,"cmsadmin/assignproject.html",{"res":r})#{"m":r1}
	