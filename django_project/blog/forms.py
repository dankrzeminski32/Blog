from .models import Post, Feedback
from django import forms


class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        fields = '__all__'
