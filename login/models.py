from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User_Profile(models.Model):
  user = models.OneToOneField(User)
	foto = models.ImageField(upload_to = 'foto_perfil/', blank = True)

	def __str__(self):

		return self.user.username