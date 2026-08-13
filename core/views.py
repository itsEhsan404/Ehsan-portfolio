from django.shortcuts import render


def home(request):
    context = {
        'name': 'Ehsan',
        'age': 20,
        'course':'Camputer Engineering',
    }

    return render(request, 'core/home.html', context)
