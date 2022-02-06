from django.shortcuts import render
from .models import UpperSection, MidSection, LowerSection


# Create your views here.
def upper(request):
    context = { 'greeting': UpperSection.objects.all(), }

    return render(request, 'UpperSection.html', context)


def mid(request):
    context = { 'about': MidSection.objects.all(), }

    return render(request, 'MidSection.html', context)


def lower(request):
    context = { 'team': LowerSection.objects.all(), }

    return render(request, 'LowerSection.html', context)
