from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.contrib.auth.models import User
import os

# Create your models here.

 

# creation la classe Utilisateur

class Utilisateur(models.Model):

    ville = models.CharField(max_length=100, null=True)
    telephone = models.CharField(max_length=100, null=True)
    photoProfil = models.ImageField(upload_to='image/profile_pics/', default='default.jpeg', blank=True)
    question = models.CharField(max_length=100)
    reponse = models.CharField(max_length=100)

    # pour que la classe ne crée pas une table dans la BD
    class Meta:
        abstract = True
    


# creation de la Classe Etudiant

class Etudiant(Utilisateur):
    # User possede déja : username, email, first_name, last_name, (password 1 et 2)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='etudiant')

    NIVEAUX = [
        ('BAC + 1', 'BAC + 1'),
        ('BAC + 2', 'BAC + 2'),
        ('BAC + 3', 'BAC + 3'),
        ('BAC + 4',  'BAC + 4'),
        ('BAC + 5', 'BAC + 5'),
        ('Doctorant', 'Doctorant'),
    ]
    niveauEtude = models.CharField(choices=NIVEAUX, default='BAC + 1', max_length=100)
    universite = models.CharField(max_length=100)
    fiche_inscription = models.FileField(upload_to='documents/fiches_inscription', blank=True)
    bio = models.TextField(max_length=300, null=True, blank=True, default="Je suis un étudiant de l'UNIVERSITÉ DE YAOUNDÉ 1. Je suis assez ambitieux et jai des projets que je souhaiterais mettre sur le marché.")
    def __str__(self):
        return f'{self.user.username} Profile'



# creation de la classe Investisseur

class Investisseur(Utilisateur):
    # User possede déja : username, email, first_name, last_name, (password 1 et 2)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='investisseur')

    profession = models.CharField(max_length=100)
    objectifs = models.CharField(max_length=300)
    entreprise = models.CharField(max_length=100, blank=True, default='Non renseigné')
    def __str__(self):
        return f'{self.user.username} Profile'
