from django.forms import ModelForm
from mailing.forms import StyleFormMixin
from blog.models import Blog


class BlogForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Blog
        exclude = ('views_count', 'owner')
