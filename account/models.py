from django.db import models

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser


ACCOUNT_TYPES = (
    ('agent', 'Agent'),
    ('employer', 'Employer')
)

    
class UserManager(BaseUserManager):
    """Define a model manager for a custom user"""

    def _create_user(self, username, password=None, **extra_fields):
        
        
        # email = self.normalize_email(email)
        user = self.model(username= username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password=None, **extra_fields):
        """Create a superuser with NID,  email, phone and password"""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_admin", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username, password, **extra_fields)
    
    
class CustomUser(AbstractUser):    
    username = models.CharField(verbose_name="Username", max_length=250, unique= True) 
       
    firstname = models.CharField(max_length = 5000, null=True)
    lastname = models.CharField(max_length = 5000, null=True)
    phone= models.CharField( max_length=50,null=True)
       
    email = models.EmailField(
        max_length=254,
        unique= True,        
        error_messages={
            "required": "Your email please!",
            "unique": "This Email address is already in use.",
        },       
        
    )
    
    account_type = models.CharField(verbose_name='Account Type'
                                    , max_length=250, choices=ACCOUNT_TYPES, default='employer')
   
    password = models.CharField(verbose_name="Password", max_length=150, null=False)
    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    

    objects = UserManager()

    USERNAME_FIELD = "username"

    REQUIRED_FIELDS = ["firstname","lastname","email", "password"]

    def __str__(self):
        return f"(%s)" % (self.firstname)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    
    
class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True)
    image = models.ImageField(default="default.jpg", upload_to=f"profiles/{user.name}")

    def __str__(self):
        return f"Profile for {self.user.nid}"

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
    