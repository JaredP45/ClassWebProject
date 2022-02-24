from django.shortcuts import render
from .models import UpperSection, MidSection, LowerSection


def base(request):
    context = {
        'greeting': UpperSection.objects.all(),
        'about': MidSection.objects.all(),
        'team': LowerSection.objects.all(),
    }

    return render(request, 'base.html', context)
