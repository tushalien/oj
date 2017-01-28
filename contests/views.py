from django.shortcuts import render
from . import models, forms
# Create your views here.
def home(request):

 	return render(request, "contests/base.html")

# def add(request):
#     class AdminPost(View):
#     #template_name = ''

#@method_decorator(login_required)
def add(request, form=None):
    data = {}
    form_data = {}
    # if pk:
    #     try:
    #         pk = int(pk)
    #         post = models.Post.objects.get(pk=pk)
    #         checker = ObjectPermissionChecker(request.user)
    #         if not request.user.has_perm('main.change_post') \
    #             and not checker.has_perm('change_post', post):
    #             return HttpResponse('Forbidden')

    #         form_data['title'] = post.title
    #         form_data['content'] = post.raw
    #         form_data['abstract'] = post.abstract
    #         form_data['author_id'] = post.author.id
    #         data['edit_flag'] = True
    #     except models.Post.DoesNotExist:
    #         raise Http404
    # else:
    #     post = None
    # if not form:
    form = forms.AddContest(initial=form_data)
    data['form'] = form
    # data['posted_tags'] = [tag for tag in post.tags.all()] if post else None
    # data['posted_category'] = post.category if post else None
    # tags = models.Tag.objects.all()
    # data['tags'] = tags
    # catagories = models.Category.objects.all()
    # data['catagories'] = catagories
    # data['pk'] = pk
    return render(request,'contests/add.html', data)
			