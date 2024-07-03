from django import forms


class GetInTouchForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    subject = forms.CharField()
    message = forms.CharField()


class MessageForm(forms.Form):
    name = forms.CharField()
    tel = forms.CharField()
    email = forms.EmailField()
    city = forms.CharField()
    message = forms.CharField()
    agree = forms.BooleanField()
