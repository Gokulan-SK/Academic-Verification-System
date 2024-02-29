# models.py

from django.db import models
from django.contrib.auth.models import User

class DocumentSubmission(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('STUDENT_NOT_FOUND', 'Student not found'),
        ('NOT_ORIGINAL', 'Not Original')
    )
    roll_number = models.CharField(max_length=20)
    transcript = models.FileField(upload_to='transcripts/')
    transcript_hash = models.CharField(max_length=64)  # Store hash of transcript
    certificate = models.FileField(upload_to='certificates/')
    certificate_hash = models.CharField(max_length=64)  # Store hash of certificate
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    submission_time = models.DateTimeField(auto_now_add=True)
    faulty_document = models.CharField(max_length=50, blank=True, null=True)  # Store the problematic document
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE)
