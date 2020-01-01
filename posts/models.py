from django.db import models


class Post(models.Model):
    title = models.TextField()
    link = models.CharField(max_length=300, null=True)
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title