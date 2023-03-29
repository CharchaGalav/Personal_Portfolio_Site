from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class UserProfile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    avatar = models.FileField(upload_to='avatars', blank=True)
    bio = models.TextField(blank=True)
    resume = models.FileField(upload_to='resumes', blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
class CodingProfiles(models.Model):
    class Meta:
        ordering = ['name']
    
    name = models.CharField(max_length=200)
    link = models.URLField(blank=True)
    icon = models.FileField(upload_to='CodingProfile', blank=True)

    def __str__(self):
        return self.name
    
class Skill(models.Model):
    name = models.CharField(max_length=50)
    efficiency = models.IntegerField(blank=True, null=True)
    icon = models.FileField(upload_to='skills', blank=True)
    is_key_skill = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class Certificate(models.Model):
    class Meta:
        ordering = ['date']

    name = models.CharField(max_length=200)
    description = RichTextField(blank=True)
    link = models.URLField(blank=True)
    date = models.DateTimeField(blank=True, null=True)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Education(models.Model):
    class Meta:
        ordering = ['-date']

    institution = models.CharField(max_length=300)
    year = models.CharField(max_length=50, blank=True)
    date = models.DateTimeField(blank=True, null=True)
    location = models.CharField(max_length=200)
    link = models.URLField(blank=True)
    description = RichTextField(blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.institution

class Experience(models.Model):
    class Meta:
        ordering = ['-date']

    company = models.CharField(max_length=300)
    year = models.CharField(max_length=50, blank=True)
    date = models.DateTimeField(blank=True, null=True)
    location = models.CharField(max_length=200)
    description = RichTextField(blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.company
    
class Project(models.Model):
    class Meta:
        ordering = ['-date']

    name = models.CharField(max_length=300)
    date = models.DateTimeField(blank=True, null=True)
    description = RichTextField(blank=True)
    link = models.URLField(blank=True)
    image = models.FileField(upload_to='projects', blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class CertificateImages(models.Model):
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.image.name
    
    
class Blog(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    content = RichTextField()

    def __str__(self):
        return self.title
    
class Contact(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
    
    
