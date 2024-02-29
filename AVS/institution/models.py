import hashlib
from django.db import models

class Student(models.Model):
    roll_number = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=100)
    graduation_date = models.DateField()
    enrollment_date = models.DateField()
    course = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    degree_certificate = models.FileField(upload_to='degree_certificates/')
    transcript = models.FileField(upload_to='transcripts/')
    degree_certificate_hash = models.CharField(max_length=64, blank=True)
    transcript_hash = models.CharField(max_length=64, blank=True)

    def save(self, *args, **kwargs):
        if self.degree_certificate:
            self.degree_certificate_hash = self.compute_hash(self.degree_certificate)
        if self.transcript:
            self.transcript_hash = self.compute_hash(self.transcript)
        super().save(*args, **kwargs)

    def compute_hash(self, file):
        hasher = hashlib.sha256()
        for chunk in file.chunks():
            hasher.update(chunk)
        return hasher.hexdigest()

    def __str__(self):
        return self.name
