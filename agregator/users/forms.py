from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import CustomUser


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    study_direction = forms.ChoiceField(choices=CustomUser.STUDY_DIRECTIONS,
        label="Направление учебы")

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'study_direction')


class StudyDirectionForm(forms.ModelForm):
    study_direction = forms.ChoiceField(
        choices=CustomUser.STUDY_DIRECTIONS,
        label="Направление учебы"
    )

    class Meta:
        model = CustomUser
        fields = ['study_direction']
