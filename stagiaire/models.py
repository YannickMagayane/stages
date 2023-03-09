from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import os

type_gender = (
    ('homme', 'Homme'),
    ('femme', 'Femme'),
)


class Filiaire(models.Model):
    filiaire = models.CharField(max_length=50,unique=True )
    bureau = models.CharField(max_length=50)

    def __str__(self):
        return self.filiaire


    def get_absolute_url(self):
        return reverse('filiaire_list')



def renomer_image(instance, filename):
    upload_to = 'image/'
    # nom_utilisateur.extension
    ext = filename.split('.')[-1]
    if instance.user.username and instance.user.first_name:
        filename = "photo_passeport/{} {}.{}".format(instance.user.username, instance.user.first_name, ext)
    return os.path.join(upload_to, filename)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    promotion = models.CharField(max_length=50)
    photo = models.ImageField(upload_to=renomer_image)
    option = models.ForeignKey(Filiaire, on_delete=models.CASCADE)
    sex = models.CharField(max_length=50, choices=type_gender, default='homme')
    start_stage = models.DateTimeField(default=timezone.now)
    end_stage = models.DateField()


    def __str__(self):
        return str(self.user) + ' ' + str(self.option)

    def get_absolute_url(self):
        return reverse('filiaire_list')



class Program(models.Model):
    programme = models.CharField(max_length=50)
    option = models.ForeignKey(Filiaire, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return self.programme

    def get_absolute_url(self):
        return reverse('filiaire_list')
