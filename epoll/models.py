# from typing_extensions import Required
from django.db import models
from pkg_resources import require
from accounts.models import * 
from cloudinary.models import CloudinaryField

# Create your models here.
class Voter(models.Model):
    # admin = models.ManyToManyField(CustomUser, on_delete=models.CASCADE)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    # name = models.CharField(max_length=255)
    identification_number=models.IntegerField(unique=True)
    phone = models.CharField(max_length=11)  
    email = models.EmailField(max_length=255)
    otp = models.CharField(max_length=10, null=True)
    verified = models.BooleanField(default=False)
    voted = models.BooleanField(default=False)
    otp_sent = models.IntegerField(default=0) 

    def __str__(self):
        return self.user.last_name + ", " + self.user.first_name


class Position(models.Model):
    position_name = models.CharField(max_length=50, unique=True)
    max_vote = models.IntegerField()
    priority = models.IntegerField()

    def __str__(self):
        return self.position_name


class Candidate(models.Model):
    fullname = models.CharField(max_length=50)
    image = CloudinaryField('image', folder = "avatar/",)
    bio = models.TextField()
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return self.fullname

class Votes(models.Model):
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)