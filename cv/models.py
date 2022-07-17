from pyexpat import model
from unicodedata import category
from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Tag(models.Model):
    tag_text = models.CharField(max_length=20)
    def __str__(self):
        return self.tag_text
    
class Category(models.Model):
    category_name = models.CharField(max_length=25)
    category_image = models.ImageField(upload_to='media/uploads/',null=True)
    category_order = models.IntegerField(null=True)
    def __str__(self):
        return self.category_name

class Post(models.Model):
    post_title = models.CharField(max_length=50)
    post_description = RichTextField(null=True)
    post_content = RichTextField(null=True)
    post_image = models.ImageField(upload_to='media/uploads/',null=True)
    category = models.ForeignKey(Category,on_delete=models.PROTECT,null=True)
    tags = models.ManyToManyField(Tag) 
    def __str__(self):
        return self.post_title

class Skill(models.Model):
    skill_text = models.CharField(max_length=25)
    skill_level = models.IntegerField()
    def __str__(self):
        return self.skill_text

class Profile(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    birth_day = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    description = RichTextField(null=True)
    picture = models.ImageField(upload_to='media/uploads/',null=True)
    github = models.CharField(max_length=50)
    transcription = models.FileField(upload_to='media/uploads/',null=True)
    def __str__(self):
        return self.first_name + " " +  self.last_name

class Referee(models.Model):
    title = models.CharField(max_length=25)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    company = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    def __str__(self):
        return self.first_name + " " +  self.last_name