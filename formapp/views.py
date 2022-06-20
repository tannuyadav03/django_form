from distutils.log import error
from django.shortcuts import render
from formapp.forms import StudentForm
from django.http import HttpResponse
from django.http import HttpResponseNotFound


def form_request(request):
    # Check the form is submitted or not
    if request.method == 'POST':
        student = StudentForm(request.POST)
        # Check the form data are valid or not
        if student.is_valid():
            # Read the submitted values
            name = 'Tannu Yadav'
            # Merge the values
            data = ['You have logged in successfully.<br />', 'Name:', name,]
            # Return the form values as response
            return HttpResponse(data)

        else:
             return HttpResponseNotFound('Error')
            #  render(request, 'form_error.html', {'form': student})
    else:
        # Display the html form
        student = StudentForm()
        return render(request, "form.html", {'form': student})
# Create your views here.
