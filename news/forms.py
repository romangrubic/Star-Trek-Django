from django import forms
from .models import News, NewsComment


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('author',
                  'title',
                  'content',
                  'image',
                  'tag',
                  'published_date')


class NewsCommentForm(forms.ModelForm):
    class Meta:
        model = NewsComment
        fields = ('content',)
