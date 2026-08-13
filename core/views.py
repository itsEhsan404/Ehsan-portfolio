from django.shortcuts import render


def home(request):
    context = {
        'name': 'Ehsan',
    }

    return render(request, 'core/home.html', context)
