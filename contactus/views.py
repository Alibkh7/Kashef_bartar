from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from contactus.forms import ContactForm
from contactus.models import Team


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_app:home')
    else:
        form = ContactForm()

    return render(request, 'contactus/contact.html', {'form': form})


def about_view(request):
    teams = Team.objects.all()
    return render(request, 'contactus/about.html', {'teams': teams})
