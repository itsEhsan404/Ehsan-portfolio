from django.shortcuts import render

from .models import Project
from .forms import ContactMessageForm


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

    for project in projects:
        project.technology_list = [
            technology.strip()
            for technology in project.technology.split(',')
            if technology.strip()
        ]

    context = {
        'projects': projects,
    }

    return render(request, 'core/projects.html', context)


def contact(request):

    if request.method == 'POST':

        form = ContactMessageForm(request.POST)

        if form.is_valid():

            form.save()

            return render(
                request,
                'core/contact.html',
                {
                    'form': ContactMessageForm(),
                    'success': True,
                }
            )

    else:

        form = ContactMessageForm()

    return render(
        request,
        'core/contact.html',
        {
            'form': form,
        }
    )