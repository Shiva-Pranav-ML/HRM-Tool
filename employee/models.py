from django.db import models

class Employee(models.Model):
    emp_id = models.IntegerField(primary_key=True,unique=True)
    emp_name = models.TextField()
    emp_category = models.TextField()
    rm_id = models.IntegerField(unique=True)

    class Meta:
        db_table = 'employee'

class RmRequested(models.Model):
    trn_name = models.TextField()
    urgency = models.IntegerField()
    emp_id = models.IntegerField()
    tm_acceptance = models.TextField()
    rej_reason = models.TextField()
    session_date = models.TextField()
    session_time = models.TextField()

    class Meta:
        db_table = 'rm_requested'
