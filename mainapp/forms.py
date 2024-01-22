from django import forms

from mainapp.models import Student


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        # fields = '__all__'
        fields = ('first_name', 'last_name', 'avatar', 'email',)
        exclude = ('is_active',)
