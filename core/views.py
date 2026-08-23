from django.shortcuts import render

from .models import Project


def home(request):
    context = {
        'name': 'Ehsan',
        'age': 21,
        'course': 'Computer Engineering',
        'courses': [
            {
                'name': 'Python',
                'duration': '3 months',
                'level': 'Beginner',
            },
            {
                'name': 'Django',
                'duration': '2 months',
                'level': 'Intermediate',
            },
            {
                'name': 'Git',
                'duration': '1 month',
                'level': 'Beginner',
            },
        ],
    }

    return render(request, 'core/home.html', context)
def about(request):
    return render(request, 'core/about.html')

def projects(request):
    projects = Project.objects.all()
    context = {
        'projects': projects,
    }
    return render(request, 'core/projects.html', context)
