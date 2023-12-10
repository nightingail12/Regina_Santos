from django.db import models

class crudst(models.Model):
    contact_name = models.CharField(max_length=100)
    contact_email = models.EmailField()
    contact_notes = models.CharField(max_length=500)
    contact_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contact_name


