from django.shortcuts import render
from .models import UpperSection, MidSection, LowerSection


def base(request):
    context = {
        'about': MidSection.objects.all(),
        'team': LowerSection.objects.all(),
    }

    return render(request, 'base.html', context)


def upper(request):
    context = {'greeting': UpperSection.objects.all()}
    return render(request, 'UpperSection.html', context)
