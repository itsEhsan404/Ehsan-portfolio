from django.shortcuts import render, get_object_or_404

from .models import post


def blog(request):
    posts = post.objects.all().order_by('-created_at')

    context = {
        'posts': posts,
    }

    return render(request, 'blog/blog.html', context)


def post_detail(request, post_id):
    Post = get_object_or_404(post, id=post_id)

    context = {
        'post': Post,
    }

    return render(request, 'blog/post_detail.html', context)