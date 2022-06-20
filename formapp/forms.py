# Import form modules
from unicodedata import name
from django import forms
from django.core.exceptions import ValidationError

# Create class to define the form fields
class StudentForm(forms.Form):
    name = forms.CharField(label="Enter name", max_length=40)
    error_messages = {
                 'required':"Please Enter Correct Name"
                 }
    def clean_name(self):
        data = self.cleaned_data['name']
        if "Tannu Yadav" != data:
            raise ValidationError("Error")
        return data

# def is_valid(self):
#     valid = 'Tannu Yadav'.is_valid()
#     # super(UserForm,self).is_valid()
#     if valid:
#         return True
#     else:
#         return False


# def is_valid(self):
#         name = self.cleaned_data['Tannu Yadav']
       
#         if name != 'Tannu Yadav':
#             raise ValidationError
        
#         return super(StudentForm, self).clean()

def clean_name(self):
        data = self.cleaned_data['name']
        if "Tannu Yadav" not in data:
            raise ValidationError("Error")

