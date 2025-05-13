from django.db import models

# Create your models here.


class Employee(models.Model):

    employee_name = models.CharField(max_length=40)
    employee_salary = models.IntegerField()
    employee_mobile = models.CharField(max_length=15)
    employee_address = models.TextField()
    employee_role = models.CharField(max_length=40, default="Employee")

    def __str__(self):
        return f"Employee name is {self.employee_name}"

class Manager(models.Model):
    manager_name = models.CharField(max_length=40)
    manager_salary = models.IntegerField()
    manager_responsibility = models.TextField()

    def __str__(self):
        return self.manager_name


