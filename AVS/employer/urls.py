from django.urls import path
from . import views

urlpatterns = [
    path('request-submission/', views.request_submission, name='request_submission'),
    path('submissions/',views.submissions, name='submissions'),
    path('emp-home/',views.employer_home,name='employer_home'),
    # Add other URL patterns as needed
]
