from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
from courses.models import Course

class Message(models.Model):
    course = models.ForeignKey(Course, related_name='courses_m', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses_m')
    message = models.TextField()
    date_added  = models.DateTimeField(default=timezone.now().isoformat())

    class Meta:
        ordering = ['date_added']