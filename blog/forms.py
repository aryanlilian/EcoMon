from django import forms
from .models import Comment, Post

class PostCreateForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(), max_length=200)
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 25, 'cols': 50}))

    class Meta:
        model = Post
        exclude = ['author', 'slug', 'published_date', 'updated_date']
