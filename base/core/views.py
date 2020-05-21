from django.shortcuts import render
from django.http import HttpResponse
from core.models import Person, Profile, Skills, Experience, Education, Projects
from core.forms import ContactForm
from django.core.mail import send_mail, BadHeaderError


def index(request):
    try:
        person = Person.objects.get(pk=1)
    except:
        return render(request, "error.html")

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
        'projects': projects,
        'form': ContactForm()
    }

    return render(request, "index.html", context)


def contact(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        subject = form.cleaned_data['subject']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']
        try:
            send_mail(subject=subject, message=message, from_email=email, recipient_list=['armarmaanmalik@gmail.com'], fail_silently=False)
            return HttpResponse('OK', status=200)
        except BadHeaderError:
            return HttpResponse(status=400)
    else:
        return HttpResponse(status=400)