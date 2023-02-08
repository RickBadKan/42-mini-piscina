from django import forms


class PlainText(forms.Form):
    plain_text = forms.CharField(label='PlainText')