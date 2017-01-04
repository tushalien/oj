from django.db import models

# Create your models here.
class logindb(models.Model):
	fname=models.CharField(max_length=100)
	lname=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	passwrd=models.CharField(max_length=100)

	def __unicode__(self):
		return self.email

class Person(models.Model):
	name=models.CharField(max_length=20)
	add=models.CharField(max_length=10)