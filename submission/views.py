from django.shortcuts import render

# from .forms import SubmitForm
#from judge import runjudge
# from .models import Submit,Runs
from subprocess import Popen, PIPE

def solve(request,pk):
	form = SubmitForm(request.POST or None)
	if form.is_valid():

		request.session['code'] = pk
		instance = form.save(commit=False)
		#print form.cleaned_data.get("code")
		instance.save()
	context = {
		"form" : form
	}
	return render(request,"submit.html",context)

def solved(request):
	if request.method=='POST':
		lang=request.POST['language']
		code=request.POST['code']
		uid=2
		pid=2
		sub=Submit(language=lang,code_upload=code,code=pid)
		sub.save()
		# run=Runs(language=lang,pid=pid,tid=uid)
		# run.save()
		rid=42
		#runjudge(rid)

		cmd = "python3 /home/tushalien/Desktop/final/login/submission/judge.py "+str(rid)
		p = Popen(cmd , shell=True, stdout=PIPE, stderr=PIPE)
		out, err = p.communicate()
		print "Return code: ", p.returncode
		print out.rstrip(), err.rstrip()


		# form = SubmitForm(request.POST or None)
		# if form.is_valid():
		# 	instance = form.save(commit=False)
		# 	#print form.cleaned_data.get("code")
		# 	instance.save()
		# context = {
		# 	"form" : form
		# }
		return render(request,"submission.html")
	else:
		return render(request,"submissions.html")

