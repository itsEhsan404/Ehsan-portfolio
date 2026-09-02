from django.shortcuts import render, get_object_or_404, redirect

from .models import post


def blog(request):
    posts = post.objects.all().order_by('-created_date')

    context = {
        'posts': posts,
    }

    return render(request, 'blog/blog.html', context)


def post_detail(request, slug):
    if slug.isdigit():
        Post = get_object_or_404(post, pk=slug)
        return redirect('post_detail', slug=Post.slug, permanent=True)
    else:
        Post = get_object_or_404(post, slug=slug)

    context = {
        'post': Post,
    }

    return render(request, 'blog/post_detail.html', context)