from django.shortcuts import render, redirect, get_object_or_404
from .forms import StudentForm
from .models import Student
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseNotAllowed
from employer.models import DocumentSubmission


@login_required
def home(request):
    #if the user is not authorized render a 404 not found page
    if request.user.username != 'admin':
        return render(request,'authenticate/404notfound.html',status=404)
    return render(request, 'institution/dashboard.html', {})

@login_required
def delete_student(request):

    #if the user is not authorized render a 404 not found page
    if request.user.username != 'admin':
        return render(request,'authenticate/404notfound.html',status=404)
    
    error_message = ""
    success_message = ""
    if request.method == 'POST':
        roll_number = request.POST.get('roll_number')

        if Student.objects.filter(roll_number=roll_number).exists():
            student = Student.objects.get(roll_number=roll_number)
            student.delete()
            print("deletion")
            success_message = 'Student record deleted successfully.'
        else:
            print("not found")
            error_message = "Student record not found."

        context={
            'success_message' : success_message,
            'error_message' : error_message
        }
        return render(request,'institution/delete-student.html',context)

    elif request.method == 'GET':
        return render(request, 'institution/delete-student.html')

    return HttpResponseNotAllowed(['GET', 'POST'])


@login_required
def all_submissions(request):
    #if the user is not authorized render a 404 not found page
    if request.user.username != 'admin':
        return render(request,'authenticate/404notfound.html',status=404)
    # Retrieve all document submissions
    all_submissions = DocumentSubmission.objects.all()
    
    # Pass the submissions to the template
    context = {
        'all_submissions': all_submissions
    }
    
    # Render the template with the context
    return render(request, 'institution/all-submissions.html', context)



@login_required
def modify_student(request):

    #if the user is not authorized render a 404 not found page
    if request.user.username != 'admin':
        return render(request,'authenticate/404notfound.html',status=404)
    
    if request.method == 'GET':
        return render(request, 'institution/modify-student.html')

    elif request.method == 'POST':

        success_message=''
        error_message=''
        roll_number = request.POST.get('roll_number')

        if not Student.objects.filter(roll_number=roll_number).exists():
            error_message="record not found."
            return render(request,'institution/modify-student.html',{'error_message': error_message} )
        
        form = StudentForm(request.POST, request.FILES, instance=roll_number)
        if form.is_valid():
            form.save()
            # Add a success message
            success_message='record modified successfully'
        else:
            students = Student.objects.all()

        context = {
            'success_message' : success_message,
            'error_message' : error_message,
            'form': form,
            'students': students,
        }
        return render(request, 'institution/modify-student.html', context)



@login_required
def add_student(request):
    #if the user is not authorized render a 404 not found page
    if request.user.username != 'admin':
        return render(request,'authenticate/404notfound.html',status=404)
    error_message = ''
    success_message = ""

    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            roll_number = form.cleaned_data['roll_number']
            if Student.objects.filter(roll_number=roll_number).exists():
                error_message = "A student with the same roll number already exists."
            else:
                name = form.cleaned_data['name']
                graduation_date = form.cleaned_data['graduation_date']
                enrollment_date = form.cleaned_data['enrollment_date']
                course = form.cleaned_data['course']
                degree = form.cleaned_data['degree']
                degree_certificate = form.cleaned_data['degree_certificate']
                transcript = form.cleaned_data['transcript']

                student = Student.objects.create(
                    roll_number=roll_number,
                    name=name,
                    graduation_date=graduation_date,
                    enrollment_date=enrollment_date,
                    course=course,
                    degree=degree,
                    degree_certificate=degree_certificate,
                    transcript=transcript
                )
                success_message = "Student record added successfully."
    else:
        form = StudentForm()

    context = {
        'form': form,
        'error_message': error_message,
        'success_message': success_message,
    }

    return render(request, 'institution/add-student.html', context)
