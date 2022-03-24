from django.shortcuts import render

from .forms import ContactForm
from .models import UpperSection, MidSection, LowerSection


def base(request):
    context = {
        'greeting': UpperSection.objects.all(),
        'about': MidSection.objects.all(),
        'team': LowerSection.objects.all(),
        'form': ContactForm,
    }

    return render(request, 'base.html', context)
