from django.shortcuts import render
from cmsadmin.models import Clint
from cmsadmin.models import Managers

def index(request):
		return render(request,"devloper/index.html")

