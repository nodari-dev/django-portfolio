from django.db import models

class Message(models.Model):
    name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150, null=True)
    email = models.EmailField()
    text = models.TextField()

    def __str__(self):
        return (self.name + " " + self.last_name)