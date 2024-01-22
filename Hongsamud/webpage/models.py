from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
CATEGORY = (
    ("01", "Novels"),
    ("02", "Kids"),
    ("03", "Academic"),
    ("04", "Magazine"),
    ("05", "Doujin"),
    ("06", "Cartoon"),
    ("07", "Religion"),
)
GENRES = (
    ("Horror", "Horror"),
    ("Thriller", "Thriller"),
    ("Romance", "Romance"),
    ("Sci-fi", "Sci-fi"),
    ("Fantasy", "Fantasy"),
    ("Mystery", "Mystery"),
    ("Food", "Food"),
    ("Comedy", "Comedy"),
    ("Action", "Action"),
    ("self-improvement", "self-improvement"),
)


class Author(models.Model):
    # id auto generate by django
    name = models.CharField(max_length=50)
    book_count = models.IntegerField(default=0)
    def __str__(self):
        return str(self.id) + "-" + self.name
    
class Publisher(models.Model):
    # id auto generate by django
    name = models.CharField(max_length=50)
    def __str__(self):
        return str(self.id) + "-" + self.name

class Book(models.Model):
    id = models.CharField(primary_key=True, max_length=6, validators=[MinLengthValidator(6)]) # type 00 increment number 0000
    name = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE) #fk
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE) #fk
    category = models.CharField(max_length=20, choices=CATEGORY) # 01 - 07
    genre = models.CharField(max_length=20, choices=GENRES)
    quantity = models.IntegerField()
    description = models.TextField(null=True)
    image = models.ImageField(upload_to="images/", null=True)

    def __str__(self):
        return self.id