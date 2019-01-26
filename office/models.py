from django.db import models
from authorization.models import *


class Group(models.Model):
    number = models.IntegerField(max_length=4, unique=True)
    slug = models.SlugField(max_length=120)

    def __str__(self):
        return "Група - {}".format(self.number)


class Subject(models.Model):
    name = models.CharField(max_length=120)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=120)

    def __str__(self):
        return "Предмет - {}, група - {}".format(self.name, self.group.number)

    def get_absolute_url(self):
        return "/subject/{}/".format(self.slug)


def file_folder(instance, filename):
    filename = instance.title + '.' + filename.split('.')[1]
    return "files/{0}".format(filename)


class Files(models.Model):
    file = models.FileField(upload_to=file_folder)
    title = models.CharField(max_length=120)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.title)

    def get_absolute_url(self):
        return "/media/{}".format(self.file)


class Teacher(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject)
    files = models.ManyToManyField(Files)

    def __str__(self):
        return "{} {} {}".format(self.profile.name, self.profile.surname, self.profile.last_name)
