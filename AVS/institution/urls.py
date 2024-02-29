from django.urls import path
from . import views

urlpatterns = [
    path('add-student/', views.add_student, name='add_student'),
    path('institution-home/',views.home,name='institution_home'),
    path('modify-student/', views.modify_student, name='modify_student'),
    path('delete-student',views.delete_student,name='delete_student'),
    path('all-submissions',views.all_submissions, name='all_submissions'),
    # Add other URL patterns as needed
]
