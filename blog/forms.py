from django import forms
from .models import Post, Comment
from common.constants import help_texts

class PostCreateForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(),
        max_length=200,
        help_text=help_texts['post_title']
    )
    content = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 25, 'cols': 50}),
        help_text=help_texts['any_character']
    )

    class Meta:
        model = Post
        exclude = ['author', 'slug', 'published_date', 'updated_date']


class CommentUpdateForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.TextInput(attrs={'class' : 'form-control w-100', 'id' : 'commentContent', 'rows': 25, 'cols': 50}),
        help_text=help_texts['any_character'],
        label=''
    )

    class Meta:
        model = Comment
        fields = ['content']
