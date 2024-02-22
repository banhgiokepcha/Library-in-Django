
from django.db import models
from django.contrib import auth, admin
from django.urls import reverse
from django.contrib.auth.models import Permission, User
from django.utils.text import slugify

admin.site.register(Permission)

# Create your models here. 

class Member(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    profile_pic = models.ImageField(null=True, upload_to='profile_pic')
    
    def __str__(self):
        return f"{self.user}"
    
     
class Genre(models.Model):
    name = models.CharField(
        max_length = 200,
        help_text = 'Enter a book genre'
    )
     
    def __str__(self):
        return self.name
    
DEFAULT = 'covers/book-default-cover.jpg'
   
class Book(models.Model): 
    title = models.CharField(max_length=200)     
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(null=True)
    cover = models.ImageField(upload_to='covers', default=DEFAULT) 
    
    def __str__(self): 
        return self.title
    
    def show_author(self):
        pass
     
    def get_absolute_url(self):
        return reverse("book-detail", kwargs={"slug": self.slug})

class WantToRead(models.Model):
    title = models.CharField(max_length = 500)
    creator = models.ForeignKey(Member, on_delete = models.CASCADE)
    books = models.ManyToManyField(Book)
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now = True)
    slug = models.SlugField()
    
    def __str__(self):
        return f"{self.title} by {self.creator}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(WantToRead, self).save(*args, **kwargs) 

class Stacks(models.Model):
    creator = models.ForeignKey(Member, on_delete = models.CASCADE)
    title = models.CharField(max_length = 500)
    description = models.TextField(null=True)
    books = models.ManyToManyField(Book)
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now = True)
    
    def __str__(self):
        return f"{self.title} by {self.creator}"


class Author(models.Model): 
    name = models.CharField(max_length = 200)
    slug = models.SlugField(null=True, blank=True)
    picture = models.ImageField(null=True)
    books = models.ManyToManyField(
        Book,  
        help_text="Add books by this author"
    )
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("author-detail", kwargs={"": self.pk})


    
         
    