from django.db import models
from django.utils.timezone import now
# model named Post
class Post(models.Model):
    Male = 'M'
    FeMale = 'F'
    GENDER_CHOICES = (
        (Male, 'Male'),
        (FeMale, 'Female'),
    )

    # define a username field with bound max length it can have
    username = models.CharField( max_length = 10, blank = False, null = False)
    
    # This is used to write a post
    message = models.TextField( max_length = 50, blank = False, null = False)
    
    # Values for gender are restricted by giving choices
    gender = models.CharField(max_length = 6, choices = GENDER_CHOICES, default = Male)
    email = models.EmailField()  
    name = models.CharField( max_length = 20)
    password = models.CharField( max_length = 100)
    upload_photo = models.FileField(upload_to='mydocs', default='mydocs/myfile.pdf') 
    date = models.DateField(auto_now_add=True)





