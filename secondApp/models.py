from django.db import models

# Create your models here.


class Employee_second(models.Model):
    employee_name = models.CharField(max_length=40)
    employee_salary = models.IntegerField()
    employee_mobile = models.CharField(max_length=15)
    employee_address = models.TextField()
    employee_role = models.CharField(max_length=40, default="Employee")

    def __str__(self):
        return self.employee_name




