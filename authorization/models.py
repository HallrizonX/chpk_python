from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Docs -> https://tproger.ru/translations/extending-django-user-model/
class Profile(models.Model):
    """ Custom profile for users"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=100, blank=True, verbose_name="Ім'я")
    surname = models.CharField(max_length=100, blank=True, verbose_name="Прізвище")
    last_name = models.CharField(max_length=100, blank=True, verbose_name="По батькові")

    TYPE_OF_ACCESS = (
        ("student", 'Студент'),
        ("teacher", 'Викладач'),
    )

    
    access_profile = models.CharField(max_length=10, blank=True, choices=TYPE_OF_ACCESS)
    birth_date = models.DateField(null=True, blank=True, verbose_name="Дата народження")

    def __str__(self):
        return "{} - {} {} {}".format(self.user.id, self.surname, self.name, self.last_name)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


