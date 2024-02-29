import hashlib
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import DocumentSubmission
from institution.models import Student


@login_required
def request_submission(request):
    #if the user is not authorized render a 404 not found page
    if request.user.username == 'admin':
        return render(request,'authenticate/404notfound.html',status=404)
    if request.method == 'POST':
        roll_number = request.POST.get('roll_number')
        transcript_file = request.FILES.get('transcript')
        certificate_file = request.FILES.get('certificate')
        
        # Ensure that both transcript and certificate files are provided
        if not transcript_file or not certificate_file:
            error_message = "Please provide both transcript and certificate files."
            return render(request, 'employer/request-submission.html', {'error_message': error_message})
        
        # Calculate hashes for the submitted documents
        transcript_hash = calculate_hash(transcript_file)
        certificate_hash = calculate_hash(certificate_file)
        
        # Perform verification and update status accordingly
        verification_result = verify_documents(roll_number, transcript_hash, certificate_hash)
        status = verification_result['status']
        faulty_document = verification_result.get('faulty_document')  # Get the faulty document from the verification result
        
        # If verification fails, display an error message
        if status == 'NOT_ORIGINAL':
            error_message = f"The {faulty_document} hash value does not match the original value."
            return render(request, 'employer/request-submission.html', {'error_message': error_message})
        
        # Save the submission record in the database
        submission = DocumentSubmission.objects.create(
            roll_number=roll_number,
            transcript=transcript_file,
            transcript_hash=transcript_hash,
            certificate=certificate_file,
            certificate_hash=certificate_hash,
            status=status,
            faulty_document=faulty_document,  # Store the faulty document name
            submitted_by=request.user
        )
        
        # Set a success message
        success_message = "Document submitted successfully."
        
        # Render the template with the success message
        return render(request, 'employer/request-submission.html', {'success_message': success_message})
    else:
        return render(request, 'employer/request-submission.html')


def calculate_hash(file):
    hasher = hashlib.sha256()
    for chunk in file.chunks():
        hasher.update(chunk)
    return hasher.hexdigest()


def verify_documents(roll_number, transcript_hash, degree_certificate_hash):
    # Check if a student record with the given roll number exists
    try:
        student = Student.objects.get(roll_number=roll_number)
    except Student.DoesNotExist:
        return {'status': 'STUDENT_NOT_FOUND'}
    
    # Check if the hashes of the submitted documents match the hashes stored in the student record
    if transcript_hash == student.transcript_hash and degree_certificate_hash == student.degree_certificate_hash:
        return {'status': 'APPROVED'}  # Documents match the stored hashes, verification is successful
    else:
        faulty_document = None
        if transcript_hash != student.transcript_hash:
            faulty_document = 'Transcript'
        elif degree_certificate_hash != student.degree_certificate_hash:
            faulty_document = 'Degree Certificate'
        return {'status': 'NOT_ORIGINAL', 'faulty_document': faulty_document}  # Hashes don't match, documents are not original
    

@login_required
def submissions(request):
    #if the user is not authorized render a 404 not found page
    if request.user.username == 'admin':
        return render(request,'authenticate/404notfound.html',status=404)
    user = request.user
    submissions = DocumentSubmission.objects.filter(submitted_by=user)
    return render(request, 'employer/submissions.html', {'submissions': submissions})


@login_required
def employer_home(request):
    #if the user is not authorized render a 404 not found page
    if request.user.username == 'admin':
        return render(request,'authenticate/404notfound.html',status=404)
    return render(request,'employer/emp-home.html',{})
