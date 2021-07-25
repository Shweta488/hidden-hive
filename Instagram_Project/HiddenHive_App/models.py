from django.db import models

class Setup(models.Model):
    image = models.ImageField(upload_to = 'images/')
    caption = models.TextField(max_length=(500))
