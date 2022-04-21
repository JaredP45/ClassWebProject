from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import ContactForm
from .models import UpperSection, MidSection, LowerSection, StudentSection


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
            messages.success(request, 'Message sent, talk to you soon!')
            return redirect('home')
        messages.error(request, 'The hCaptcha is invalid. Please try again.')

    context = {
        'greeting': UpperSection.objects.all(),
        'about': MidSection.objects.all(),
        'student': StudentSection.objects.all(),
        'team': LowerSection.objects.all(),
        'form': form,
    }
    return render(request, 'base.html', context)
