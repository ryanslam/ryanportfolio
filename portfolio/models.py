from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=30, default='')
    description = models.TextField(max_length=200, default='', blank=True)
    start_date = models.DateField('date started')
    image_url = models.URLField(max_length=200, default='', blank=True)

    def __str__(self):
        return self.title


class ContactInfo(models.Model):
    name = models.CharField(max_length=30, default='')
    email = models.CharField(max_length=30, default='')
    bio = models.TextField(max_length=300, default='')
    image_url = models.URLField(max_length=200, default='', blank=True)
    github_url = models.URLField(max_length=200, default='', blank=True)
    linkedin_url = models.URLField(max_length=200, default='', blank=True)

    def __str__(self):
        return self.name
