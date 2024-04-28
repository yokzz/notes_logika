from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=63)
    text = models.TextField()
    
    def __str__(self):
        return self.title