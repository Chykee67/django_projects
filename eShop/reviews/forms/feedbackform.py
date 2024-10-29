from django import forms

from reviews.models import Feedback


class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        fields = [
            "review",
        ]