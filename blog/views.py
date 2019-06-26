from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import get_object_or_404
from .models import Project


# Create your views here.

def blog(request):
    projects = Project.objects.filter(initdate__lte=timezone.now()).order_by('initdate')
    return render(request, 'Portifolio.html', {'projects': projects})

