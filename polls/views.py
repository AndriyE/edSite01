from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.core.context_processors import csrf
from  django.contrib import auth
from django.utils.translation import ugettext as _


from .models import Post,Comment,Image
from .forms import CommentForm



def index(request):
    post_list = Post.objects.order_by('-pub_date')
    auth_name = auth.get_user(request).username
    context = {'authName':auth_name, 'post_list': post_list,'username':auth.get_user(request).username}
    context.update(csrf(request))
    if request.POST:
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return HttpResponseRedirect('/polls/')
        else:
            context['login_error'] = "Акаунт не знайденно"
            return render(request,'userssys/login.html',context)
    else:
        return render(request, 'polls/index.html', context)


def addComment(request,post_id):
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.comments_post = Post.objects.get(id= post_id)
            comment.comments_auftor_name = auth.get_user(request).username
            form.save()
        return  HttpResponseRedirect('/polls/%s/' %post_id)

def post(request,post_id=1):

    coment_form = CommentForm
    coment_form.comments_post_id = post_id
    args = {}
    args.update(csrf(request))
    args['post'] = Post.objects.get(id = post_id)
    args['username']  = auth.get_user(request).username
    args['images'] = Image.objects.filter(images_post_id = post_id)
    args['comments'] = Comment.objects.filter(comments_post_id = post_id)
    args['form'] = coment_form
    return  render(request,'polls/detail.html',args)


