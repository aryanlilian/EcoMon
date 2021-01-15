from django import forms
from .models import Comment

class CommentCreateForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Comment
        fields = ['content']
