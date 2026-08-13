from django.shortcuts import render


def home(request):
    context = {
        'name': 'Ehsan',
        'age': 20,
        'course':'Camputer Engineering',
        'courses':[
            'Python',
            'Django',
            'Git',
        ],
    }

    return render(request, 'core/home.html', context)
