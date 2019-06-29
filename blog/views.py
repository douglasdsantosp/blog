from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import get_object_or_404
from .models import Experience
from .models import Formation


# Create your views here.

def blog(request):
    experiences = Experience.objects.filter(initdate__lte=timezone.now()).order_by('initdate')
    formations = Formation.objects.filter(initdate__lte=timezone.now()).order_by('initdate')
    context = {'experiences': experiences, 'formations': formations}
    return render(request, 'Portifolio.html', context)

