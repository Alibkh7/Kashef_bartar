from django.shortcuts import render, get_object_or_404
from .models import Service, Sample
from khayyam import JalaliDatetime


def serviceListView(request):
    services = Service.objects.all()
    return render(request, 'project/service.html', {'services': services})


def serviceDetailView(request, pk):
    service = get_object_or_404(Service, pk=pk)
    return render(request, 'project/service-detail.html', {'service': service})


def worksampleView(request):
    samples = Sample.objects.all()
    return render(request, 'project/sample.html', {'samples': samples})


def worksampleDetailView(request, pk):
    sample = get_object_or_404(Sample, pk=pk)
    images = sample.images.all()
    jalali_date = JalaliDatetime(sample.date).strftime('%d %B %Y، ساعت %H:%M')
    return render(request, 'project/sample-detail.html', {'sample': sample, 'images': images, 'jalali_date': jalali_date})
