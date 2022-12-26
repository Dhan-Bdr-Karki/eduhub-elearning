from django.urls import path, include
from .views import *
from rest_framework import routers

app_name = 'api'

router = routers.DefaultRouter()
router.register('courses',CourseViewSet)

urlpatterns = [
    path('subjects/', SubjectListView.as_view(),name='subject_list'),
    path('subject/<pk>/', SubjectDetailView.as_view(), name='subject_detail'),
    # path('courses/<pk>/enroll/', CourseEnrollView.as_view(), name='course_enroll'),
    path('', include(router.urls)),
]