from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify


class Usuario(AbstractUser):
    nombres= models.CharField(max_length=100) 
    apellidos= models.CharField(max_length=100) 
    numero_celular= models.IntegerField(default=0)
    numero_identificacion = models.CharField(max_length=20, unique=True)
    staff = models.BooleanField(default=False)
    foto = models.ImageField(upload_to='fotos/', null=True, blank=True)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set', 
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',  
        blank=True
    )
    def save(self, *args, **kwargs):
        if not self.username:
            base_username = slugify(f"{self.nombres} {self.apellidos}")
            username = base_username
            counter = 1

            while Usuario.objects.filter(username=username).exists():
                username = f"{base_username}{counter}"
                counter += 1

            self.username = username

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"