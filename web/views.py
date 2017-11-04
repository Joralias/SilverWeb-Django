from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import send_mail
from silverweb import settings

from .forms import (
    FanForm,
    MessageForm,
)
from .models import (
    Fan,
)


def home(request):
    return render(request, 'web/home.html', {})


def about(request):
    return render(request, 'web/about.html', {})


def blog(request):
    return render(request, 'web/blog.html', {})


def contact(request):
    return render(request, 'web/contact.html', {})


def gallery(request):
    return render(request, 'web/gallery.html', {})


def download(request):
    return render(request, 'web/download.html', {})


def new_fan(request):
    """ Stores a new mail in the database for the newsletter"""
    if request.method == "POST":
        form = FanForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.mail = form.data['mail']
            if not Fan.objects.filter(mail=post.mail).first():
                post.save()
                messages.info(request, 'You have been registered successfully!')
                subject = "Registration in SilverWave newsletter"
                msg = settings.DEFAULT_WELCOME_MESSAGE
                sender = settings.EMAIL_HOST_USER
                receiver = [post.mail]
                send_mail(subject, msg, sender, receiver)
            else:
                messages.info(request, 'You are already registered :) !')
                pass
            return redirect('home')
    else:
        return render(request, 'web/home.html')


def new_message(request):
    """ Stores a message in the database"""
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.name = form.data['name']
            post.mail = form.data['mail']
            post.text = form.data['message']
            post.save()
            messages.info(request, 'Your message have been sent!')
            subject = "Copy of your sent message to SilverWave"
            msg = "This is a copy of your message: " + 2*"\n" \
                + 20*"-" + "\n" + post.text
            sender = settings.EMAIL_HOST_USER
            receiver = [post.mail]
            send_mail(subject, msg, sender, receiver)

            if not Fan.objects.filter(mail=post.mail).first():
                # if not yet registered, do it!
                Fan.objects.create(mail=post.mail)

            return redirect('home')
    else:
        return render(request, 'web/home.html')

