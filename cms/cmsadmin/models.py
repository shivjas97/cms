from django.db import models

class Clint(models.Model):
	name = models.CharField(max_length=30)
	email = models.CharField(max_length=30)
	mobile = models.CharField(max_length=13)
	password = models.CharField(max_length=10)
	cname= models.CharField(max_length=40)
	pname = models.CharField(max_length=40)
	location = models.CharField(max_length=25)
	about = models.CharField(max_length=100)

class Managers(models.Model):
	name = models.CharField(max_length=30)
	email = models.CharField(max_length=30)
	mobile = models.CharField(max_length=13)
	password = models.CharField(max_length=10)
	gender = models.CharField(max_length=10)
	age = models.CharField(max_length=5)
	location = models.CharField(max_length=25)
	education = models.CharField(max_length=50)
	knowledge = models.CharField(max_length=50)
	exp = models.CharField(max_length=10)
	salary = models.CharField(max_length=15)
	about = models.CharField(max_length=100)

class Alogin(models.Model):
	email = models.CharField(max_length=30)
	password = models.CharField(max_length=30)
	
class Hr(models.Model):
	name = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	mobile = models.CharField(max_length=13)
	password = models.CharField(max_length=10)
	gender = models.CharField(max_length=10)
	age = models.CharField(max_length=10)
	location = models.CharField(max_length=25)
	education = models.CharField(max_length=40)
	skills = models.CharField(max_length=50)
	exp = models.CharField(max_length=10)
	salary = models.CharField(max_length=15)
	about = models.CharField(max_length=100)
	
class Project(models.Model):
	name = models.CharField(max_length=50)
	desc = models.CharField(max_length=200)
	status = models.CharField(max_length=10)
	ccom = models.CharField(max_length=40)
	date = models.CharField(max_length=25)
	type = models.CharField(max_length=25)
	estbudget = models.CharField(max_length=10)
	estamt = models.CharField(max_length=10)
	estdur = models.CharField(max_length=10)

class Devlopers(models.Model):
	name = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	mobile = models.CharField(max_length=13)
	password = models.CharField(max_length=10)
	gender = models.CharField(max_length=10)
	age = models.CharField(max_length=10)
	location = models.CharField(max_length=25)
	education = models.CharField(max_length=40)
	knowledge = models.CharField(max_length=50)
	exp = models.CharField(max_length=10)
	designation = models.CharField(max_length=20)
	salary = models.CharField(max_length=15)
	about = models.CharField(max_length=100)

class AssignProject(models.Model):
	projectid = models.CharField(max_length=30)
	managerid = models.CharField(max_length=30)
	date=models.CharField(max_length=30)
	