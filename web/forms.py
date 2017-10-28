from django import forms

from .models import (
    Fan,
    Message,
)


class FanForm(forms.ModelForm):

    class Meta:
        model = Fan
        fields = ('mail',)


class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ('name', 'mail', 'message',)
