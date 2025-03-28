from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator,MaxValueValidator

class Author(models.Model):
    author_name = models.CharField(max_length=100,unique=True,blank=False)
    date_added = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.author_name
    
    def get_books_count(self):
        return self.books.all().count()
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.author_name)
        super().save(*args,**kwargs)

class Tags(models.Model):
    tag_name = models.CharField(max_length=50,unique=True,blank=False)
    date_added = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True,blank=True, null=True)

    def __str__(self):
        return self.tag_name
    
    def get_books_with_tag_count(self):
        return self.books.all().count()
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.tag_name)
        super().save(*args, *kwargs)


class Categories(models.Model):
    category_name = models.CharField(max_length=50,unique=True,blank=False)
    date_added = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True,blank=True, null=True)

    def __str__(self):
        return self.category_name
    
    def get_books_with_category_count(self):
        return self.books.all().count()
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.category_name)
        super().save(*args, **kwargs)

class BookDetail(models.Model):
    title = models.CharField(max_length=100,unique=True,help_text='Buradan kitabın adını daxil edin', blank=False)
    author = models.ForeignKey(Author,related_name='books',on_delete=models.SET_NULL,null=True)
    tags = models.ManyToManyField(Tags, related_name='books')
    img = models.ImageField(upload_to='book_covers/',blank=False, null=True)
    category = models.ForeignKey(Categories, related_name='books', on_delete=models.SET_NULL,null=True)
    price = models.IntegerField(validators=[MinValueValidator(3),MaxValueValidator(50)],blank=False)
    publisher_date = models.IntegerField(validators=[MinValueValidator(1700),MaxValueValidator(2025)],blank=False)
    on_sale = models.BooleanField()
    description = models.TextField(blank=False)
    slug = models.SlugField(unique=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


# Create your models here.
