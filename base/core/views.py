from django.shortcuts import render
from django.http import HttpResponse
from core.models import Person, Profile, Contact, Skills, Experience, Education, Projects
from core.forms import ContactForm
from django.core.mail import send_mail, BadHeaderError


def index(request):
    context = {}

    form = ContactForm()
    context.update({'form': form})

    try:
        person = Person.objects.get(pk=1)
    except:
        return render(request, "error.html")

    try:
        profile = Profile.objects.get(person=person)
        context.update({'profile': profile})
    except:
        return render(request, "index.html", context)

    try:
        contact = Contact.objects.get(person=person)
        context.update({'contact': contact})
    except:
        return render(request, "index.html", context)

    try:
        skills = Skills.objects.filter(person=person)
        context.update({'skills': skills})
    except:
        return render(request, "index.html", context)

    try:
        experience = Experience.objects.filter(person=person)
        context.update({'experience': experience})
    except:
        return render(request, "index.html", context)

    try:
        education = Education.objects.filter(person=person)
        context.update({'education': education})
    except:
        return render(request, "index.html", context)

    try:
        projects = Projects.objects.filter(person=person)
        context.update({'projects': projects})
    except:
        return render(request, "index.html", context)

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