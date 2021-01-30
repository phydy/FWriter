from django.db import models
from django.contrib.auth.models import User
from PIL import Image

'''
class User(AbstractUser):
	is_writer = models.BooleanField(default=False)
	is_client = models.BooleanField(default=False)
'''

class Profile(models.Model):	
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')
	location = models.CharField(max_length=50, default='Nairobi')
	about = models.TextField()


	def __str__(self):
			return f'{self.user} Profile'


	def save(self, *args, **kwargs):
			super(Profile, self).save(*args, **kwargs)

'''
class Writer(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)


class Speciality(models.Model):
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=7, default='#007bff')

    def __str__(self):
        return self.name

    def get_html_badge(self):
        name = escape(self.name)
        color = escape(self.color)
        html = '<span class="badge badge-primary" style="background-color: %s">%s</span>' % (color, name)
        return mark_safe(html)
'''



# Create your models here.
