from django import forms
from .models import Post, Comment
from common.constants import help_texts, error_messages
from django.core.exceptions import ValidationError


class PostCreateForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(),
        max_length=200,
        help_text=help_texts['post_title'],
    )
    content = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 25, 'cols': 50}),
        help_text=help_texts['any_character'],
    )

    class Meta:
        model = Post
        exclude = ['author', 'slug', 'published_date', 'updated_date']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title:
            raise ValidationError(
                error_messages['required'],
                code='title_invalid'
            )
        return title

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if not content:
            raise ValidationError(
                error_messages['required'],
                code='content_invalid'
            )
        return content


class CommentUpdateForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.TextInput(attrs={'class' : 'form-control w-100', 'id' : 'commentContent', 'rows': 25, 'cols': 50}),
        help_text=help_texts['any_character'],
        label=''
    )

    class Meta:
        model = Comment
        fields = ['content']
