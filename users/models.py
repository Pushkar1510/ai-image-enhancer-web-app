from django.db import models
from django.contrib.auth.models import User
import random
import math

def generate():
    digits = [i for i in range(0, 10)]
    random_str = ""

    for i in range(6):
        index = math.floor(random.random() * 10)
        random_str += str(digits[index])
    
    return random_str

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics/')
    premium = models.BooleanField(default=False)
    trials = models.IntegerField(default=5)
    email_verified = models.BooleanField(default=False)
    security_code = models.CharField(default=generate(), max_length=6)

    def __str__(self):
        return f'{self.user.username} Profile'