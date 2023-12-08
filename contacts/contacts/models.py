from django.db import models

class crudst(models.Model):
    contact_name = models.CharField(max_length = 100)
    contact_email = models.CharField(max_length = 100)
    contact_notes = models.CharField(max_length = 500)
    contact_time = models.DateField()



