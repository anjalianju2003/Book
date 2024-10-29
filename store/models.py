from django.db import models

# Create your models here.

from django.db import models

class Book(models.Model):

    name=models.CharField(max_length=200)

    author=models.CharField(max_length=200)

    price=models.PositiveIntegerField()

    genre_options=(
        ("love","love"),
        ("horror","horror"),
        ("drama","drama"),
    )

    genre_type=models.CharField(max_length=200,choices=genre_options,default="love")
    picture=models.ImageField(upload_to="book_images",null=True)

    def __str__(self):
        return self.name