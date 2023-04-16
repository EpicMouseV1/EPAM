from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.

class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class MyUser(AbstractUser):
    USERNAME_FIELD = 'email'
    email = models.EmailField(('email address'), unique=True) 
    REQUIRED_FIELDS = [] 
    username = models.CharField(max_length=30, unique=False, blank=True, null=True)
    objects = CustomUserManager()

class Client(models.Model):
    profile = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    phone_num = models.CharField(max_length=11, unique=True)
    company_name = models.CharField(max_length=50)
    company_addr = models.CharField(max_length=100)

class Brigade(models.Model):
    profile = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    team_name2 = models.CharField(max_length=30)
    participants = models.CharField(max_length=30)
    status = models.BooleanField()

class Operator(models.Model):
    profile = models.OneToOneField(MyUser, on_delete=models.CASCADE)

class Request(models.Model):
    type = models.CharField(
        max_length=30,
        choices=(
            ('opt1', 'Установить экобокс'),
            ('opt2', 'Вывезти мусор'),
            ('opt3', 'Демонтировать экобокс'),
        )
    )
    comments = models.CharField(max_length=150, blank=True)
    open_date = models.DateTimeField()
    close_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(
        max_length=30,
        choices=(
            ('opt', 'new'),
            ('opt2', 'in progress'),
            ('opt3', 'completed'),
        ),
        default='opt'
    )
    client_id = models.ForeignKey(
        'Client',
        on_delete=models.CASCADE,
    )
