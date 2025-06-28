from django.http import HttpResponse, Http404
from django.shortcuts import render
from blogging.models import Post

def stub_view(request, *args, **kwargs):
    body = "Stub View\n\n"
    if args:
        body += "Args:\n" + "\n".join([f"\t{a}" for a in args])
    if kwargs:
        body += "Kwargs:\n" + "\n".join([f"\t{k}: {v}" for k,v in kwargs.items()])
    return HttpResponse(body, content_type='text/plain')

def list_view(request):
    posts = Post.objects.exclude(published_date__exact=None).order_by('-published_date')
    return render(request, 'blogging/list.html', {'posts': posts})

def detail_view(request, post_id):
    posts = Post.objects.exclude(published_date__exact=None)
    try:
        post = posts.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404
    return render(request, 'blogging/detail.html', {'post': post})
