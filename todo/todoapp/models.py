from django.db import models

class ContactMessage(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    question=models.TextField()
    def __str__(self):
        return self.name
    
