# import the standard Django Model
# from built-in library
from django.db import models
from datetime import datetime
# declare a new model with a name "GeeksModel"
class BukuModel(models.Model):

    # fields of the model
    title_book = models.CharField(max_length = 200)
    description_book = models.TextField()
    date_book = models.DateField(default=datetime.now)
    author_book = models.CharField(max_length = 200, default='author')
    file_book = models.FileField(upload_to='mydocs', default='mydocs/myfile.pdf')

    # renames the instances of the model
    # with their title name
    def __str__(self):
        return self.title_book


# Create your models here.
