from django.db import models

# Create your models here.
class Student(models.Model):
    student_name = models.CharField(max_length=50)
    age = models.IntegerField()
    roll_no = models.IntegerField()

    def __str__(self):
        return self.student_name