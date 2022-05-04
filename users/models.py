from django.db import models
import os
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager

class SuperUser(BaseUserManager):
    def create_superuser(self, email, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('superuser must have is_staff')
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('superuser must have is_superuser')
        
        return self.create_user(email, username, password, **extra_fields)
    
    
    def create_user(self, email, username, password, **extra_fields):
        
        if not email:
            raise ValueError('the given email is not correct')
        
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


def load_image(instance, filename):
    upload_to = 'image/'
    external = filename.split('.')[-1]
    if instance.email:
        filename = "photo_profile/{}.{}".format(instance.email, external)
        return os.path.join(upload_to, filename)

# creation de la Classe Utilsteur
class Utilisateur(AbstractBaseUser, PermissionsMixin):
    Type_User = [
        ('Investisseur', 'Investisseur'),
        ('Etudiant', 'Etudiant'),

    ]
    email = models.EmailField('email adress', unique=True)
    username = models.CharField(max_length=255, blank=True) 
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255)
    
    objects = SuperUser()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    ville = models.CharField(max_length=200, null=True)
    photo_profile = models.ImageField('Profile', upload_to=load_image ,blank=True)
    tel = models.CharField('telephone', max_length=11)

    type_user = models.CharField('type user', max_length=20, choices=Type_User, null=True, default='Etudiant')
    
    def __str__(self):
        return self.username

    # s'inscrire sur la platefoerme
    def register():
        pass
    
    # s'authentifier à son compte
    def login():
        pass
    #l'utilisateur peut modifier son profile
    def updateProfil():
        pass

    # consulter
    def consultProfil():
        pass

    #commenter une publication
    def commentPost():
        pass
    
    #liker un post
    def likerPost():
        pass

    # partager 
    def sharePost():
        pass

    # rechercher u
    def searchProjecet():
        pass

    # suivre un etudiant
    def followsStudent():
        pass

    # ajouter un projet comme favoris

    def appendFavoritProject():
        pass
    

# creation de la Classe Etudiant

class Etudiant(Utilisateur):
    niveau = [
        ('Licence 1', 'Licence 1'),
        ('Licence 2', 'Licence 2'),
        ('Licence 3', 'Licence 3'),
        ('Master I',  'Master I'),
        ('Master II', 'Master II'),
        ('Doctorant', 'Doctorant'),
    ]
    niveauEtude = models.CharField("Niveau D'Etude", choices=niveau, default='Licence 1', max_length=30)
    universite = models.CharField(max_length=100)
    fiche_inscription = models.FileField(upload_to=load_image)
    bio = models.TextField(max_length=500, null=True)

    def __str__(self):
        return self.user.username

    # l'etudiant redefini la methode register
    def register():
        pass

    # etudiant poste un projet
    def postProjet():
        pass

# creation de la classe Investisseur

class Investisseur(Utilisateur):
    profession = models.CharField(max_length=70)
    entreprise = models.CharField(max_length=100)
    objectif = models.CharField(max_length=500)

    # un etudiant peut avoir plusieurs relations avec un investisseur et vis-vers-sa
    etudiant = models.ManyToManyField(Etudiant, related_name='investisseurs', blank=True)

    def __str__(self):
        return self.user.username

    # l'investisseur redefini la methode register
    def register():
        pass

    # l'investisseur marque un projet investir
    def investProject():
        pass