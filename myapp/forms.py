from django import forms
from .models import addstudent

class addstudentForm(forms.ModelForm):
    # name=forms.CharField(label="Student name",max_length=100)
    # idno=forms.CharField(label='Student id')
    # std=forms.CharField(label='STD')
    # dob=forms.DateField(label='Date of Birth')
    # email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Email','class':"form-control"}))
    # password = forms.CharField(widget=forms.PasswordInput())
    # address = forms.CharField(
    #   label='Address',
    #   widget=forms.TextInput(attrs={'placeholder': '1234 Main St','class':"form-control"})
    # )
    # # address_2 = forms.CharField(
    # #     widget=forms.TextInput(attrs={'placeholder': 'Apartment, studio, or floor'})
    # # )

    # city = forms.CharField()
    # state = forms.ChoiceField(choices=STATES)
    # zip_code = forms.CharField(label='Zip')
    # check_me_out = forms.BooleanField(required=False)
    class Meta:
        model= addstudent
        fields= ["firstname", "lastname", "studentid", "std","email","password","phoneno","address"]

