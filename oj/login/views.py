from django.shortcuts import render,HttpResponse
from .forms import ContactForm,CodeForms
from .models import logindb,Person

# Create your views here.
def index(request):
	#print (request)
	#print ("##########")
	return render(request,'index.html',{})

def home(request):
	
	form=ContactForm()
	"""
	for i in Person.objects.all():
		print (i.name,i.add)
	"""
	return render(request,'homepage.html',{})
	try :
		fname=request.POST['fname']
		lname=request.POST['lname']
		email=request.POST['email']
		passwrd=request.POST['pass']
		datab=logindb(fname=fname,lname=lname,email=email,passwrd=passwrd)
		datab.save(force_insert=True)
		for i in logindb.objects.all():
			print (i.fname,i.lname,i.email,i.passwrd)
		#datab=logindb.objects.raw('INSERT INTO logindb(fname,lname,email,passwrd) VALUES ('+fname+","+lname+","+email+","+passwrd+");")
		#atab.save()
		return render(request,'homepage.html',{})
	except:
		email=request.POST['email']
		passwrd=request.POST['pass']
		for i in logindb.objects.all():
			print (i.fname,i.lname,i.email,i.passwrd)
		try:
			obj= logindb.objects.get(email=email)
			if obj.passwrd==passwrd:
				print ('########')
				return render(request,'homepage.html',{})
			else:
				return render(request,'index.html',{})
		except:
			#print ("geer")
			return render(request,'index.html',{})



def problems(request):
	print ("on problems######")
	return render(request,'q.html',{})

def submit(request):
	form = CodeForms()
	x=request.POST['code']
	print (request.POST['code'])
	f=open("someone.txt",'w')
	f.write(x)
	f.close()
	return HttpResponse(x)
	
