from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import (
    BaseUserManager, AbstractUser, AbstractBaseUser
)
from django.utils.translation import gettext as _

#Moedel du user manager
class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('Users must have an email address'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    #create super user
    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email, password) 
        user.admin = True 
        user.staff = True
        user.personnel = True
        user.save(using=self._db)
        return user

    #Create personnel user
    def create_personneluser(self, email, password, name, firstName, phone):
        user = self.create_user(email, password,  name, firstName, phone)
        user.staff = True
        user.personnel = True
        user.save(using=self._db)
        return user

    #Create staff user
    def create_staffuser(self, email, password, **extra_fields):
        user = self.create_user(email, password)
        user.staff = True
        user.personnel = True
        user.save(using=self._db)
        return user

GENRES= (
    ('Homme', 'Homme'),
    ('Femme', 'Femme')
 )

#Model du user
class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=50)
    firstName = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    genre = models.CharField(choices=GENRES, max_length=10)
    nation = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser
    personnel = models.BooleanField(default=False) # a superuser
    # notice the absence of a "Password field", that is built in.

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.staff

    @property
    def is_admin(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    
TYPES= (
    ('Clinique', 'Clinique'),
    ('Hopital', 'Hopital')
 )

    #Classe Etablissement
class Etablissement(models.Model):
    user_etablissement = models.ForeignKey(User, on_delete=models.CASCADE)
    nom_etablissement = models.CharField(max_length=50)
    adresse = models.CharField(max_length=100)
    localisation = models.CharField(max_length=500)
    heureDebut = models.CharField(max_length=10)
    heureFin = models.CharField(max_length=10)
    phone = models.CharField(max_length=10)
    typeEtablissement = models.CharField(max_length=50, choices=TYPES)
    prix = models.IntegerField(default=0)
    specialites = TaggableManager()

    # Classe Rendez_vous
class RendezVous(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    etablissement = models.ForeignKey(Etablissement, on_delete=models.CASCADE)
    objet = models.CharField(max_length=35)
    detail = models.TextField()
    date = models.DateField()
    specialite = TaggableManager()