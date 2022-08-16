from django import forms
from .models import Comment


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        # fields = '__all__'  # Don't Use This
        fields = [
            'content',
        ]