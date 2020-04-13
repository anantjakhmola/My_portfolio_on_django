from django.db import models

# Create your models here.
class Job(models.Model):
    # images
    image = models.ImageField(upload_to='images/')
    # summary
    summary = models.CharField(max_length=200)


# this is to add the name in sql admin so it wont show object.
    def __str__(self):
        return f"{self.summary}"