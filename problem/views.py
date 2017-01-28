from django.shortcuts import render
import os
# from .forms import EditProblemForm
from .models import Problems
from django.conf import settings
# def edit_p(request):
# 	form = EditProblemForm(request.POST or None)
# 	if form.is_valid():
# 		instance = form.save(commit=False)
# 		instance.save()
# 	context = {
# 		"form" : form
# 	}
# 	return render(request,"editproblem.html",context)
def list(request):
	query=Problems.objects.all()
	context={
		"title": "Problems",
		"problem" : query
	}
 	return render(request, "list.html",context)
def solve(request,pk):
    data={}
    try:
        prob = Problems.objects.get(code=pk)
    except prob.DoesNotExist:
        raise Http404
    data['code'] = prob.code
    data['desc'] = prob.statement
    # path=os.path.join(settings.MEDIA_ROOT,str(data['desc']))
    # with open(path, 'r') as content_file:
    # 	data['desc']= content_file.read()
    context={
    	"title":"Problem",
    	"data":data
    }



    return render(request, "problem.html", context)
