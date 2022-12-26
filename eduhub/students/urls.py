from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page

app_name = 'students'

urlpatterns = [
    path('register/', StudentRegistrationView.as_view(), name='student_registration'),
    path('courses/', cache_page(60*15)(StudentCourseListView.as_view()), name='student_course_list'),
    path('course/<pk>/',cache_page(60*15)(StudentCourseDetailView.as_view()), name='student_course_detail'),
    path('enroll-course/', StudentEnrollCourseView.as_view(), name='student_enroll_course'),
    path('course/<pk>/<module_id>/', cache_page(60*15)(StudentCourseDetailView.as_view()), name='student_course_detail_module'),
]
