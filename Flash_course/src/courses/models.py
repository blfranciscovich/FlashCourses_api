from django.db import models
"""
Course models for FlashCourse application
Database: FlashCourses- mySQL
"""
from django.db import models

class Institution(models.Model):
    ipeds = models.CharField(max_length=64, null=False, blank=False)
    institution_name = models.CharField(max_length=64, null=False, blank=False)
    location = models.CharField(max_length=64, null=False, blank=False)

    def __str__(self):
        return self.institution_name + ', ' + self.location


class Course(models.Model):
    course_number = models.CharField(max_length=24, null=False, blank=False)
    course_id = models.CharField(max_length=64, null=False, blank=False)
    parent_institution = models.ForeignKey(Institution, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.course_id

