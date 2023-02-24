from django import forms
from .models import Post

from django_summernote.widgets import SummernoteWidget

class PostWriteForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'file']
        widgets = {
            'content': SummernoteWidget(),
        }