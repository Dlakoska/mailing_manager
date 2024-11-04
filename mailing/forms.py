from django import forms
from mailing.models import Mailing, Client, Message


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if isinstance(field, forms.BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'
            if isinstance(field.widget, forms.widgets.DateTimeInput):
                field.widget.input_type = 'datetime-local'


class MailingForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Mailing
        exclude = '__all__'

class ClientForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Client
        exclude = '__all__'


class MessageForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Message
        exclude = '__all__'
