from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from .forms import ContactForm
from .models import UpperSection, MidSection, LowerSection


def base(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponse('Success! Thank you for your message.')

    context = {
        'greeting': UpperSection.objects.all(),
        'about': MidSection.objects.all(),
        'team': LowerSection.objects.all(),
        'form': form,
    }
    return render(request, 'base.html', context)
