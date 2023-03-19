from django.db import models

# Create your models here.
class Agency(models.Model):
    name=models.CharField(max_length=250)
    desc=models.TextField()
    img=models.ImageField(upload_to='pics')
    date=models.DateTimeField()

    def __str__(self):
        return self.name