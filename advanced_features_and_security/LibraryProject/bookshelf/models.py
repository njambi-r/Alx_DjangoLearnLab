from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, BaseUserManager

# Create your models here.
class Book (models.Model):
    title = models.CharField(max_length = 200)
    author = models.CharField(max_length = 100)
    publication_year = models.IntegerField()

#Defining a custom user model
#Ref:https://docs.djangoproject.com/en/4.2/topics/auth/customizing/#writing-a-manager-for-a-custom-user-model

#creating a custom user manager
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, date_of_birth=None, profile_photo=None, **other_fields ):
                #assuming that in our case, email is essential
                if not email:
                      raise ValueError('Users must have an email address')
                email = self.normalize_email(email) #convert email to lowercase
                #create an instance of user using our custom model
                user = self.model(username=username, email=email, date_of_birth=date_of_birth, profile_photo=profile_photo, **other_fields)
                user.set_password(password)
                """
                If we set user.password = password, the password will be stored in plain text (which is a security risk).
                set_password(password) encrypts the password before storing it.
                """
                user.save(using=self._db) #save user to database
                return user
                #using=self._db → Ensures compatibility when working with multiple databases.
    
    #Superusers have additional priviledges
    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True) #allows access to the django admi panel
        extra_fields.setdefault('is_superuser', True) #grants all permissions
        #setdefault ensures that if is_staff or is_superuser isn't provided,
        #they default to TRUE
        return self.create_user(username, email, password, **extra_fields)

#creating a custom user model
class CustomUser(AbstractUser):
    date_of_birth =  models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photo/',null=True, blank=True)

    #replace the default user manager with the custom methodes for
    #create_user and create_superuser that we defined in CustomUserManager()
    objects=CustomUserManager() 
    def __str__(self):
         return self.username
    #string representation defines how users will appear in Django admin



