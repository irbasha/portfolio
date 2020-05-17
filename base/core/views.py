from django.shortcuts import render
from core.models import Person, Profile, Skills, Experience, Education, Projects

def index(request):
    person = Person.objects.get(pk=1)
    profile = Profile.objects.get(person=person)
    skills  = Skills.objects.filter(person=person)
    experience = Experience.objects.filter(person=person)
    education = Education.objects.filter(person=person)
    projects = Projects.objects.filter(person=person)

    context = {
        'person': person,
        'profile': profile,
        'skills': skills,
        'experience': experience,
        'education': education,
        'projects': projects
    }
    return render(request, "index.html", context)