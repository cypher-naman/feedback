from django import forms

from .models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        exclude = []
        #exclude = ['student_name','rollno','batch','Section_name']
