from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

# from .managers import UserManager
# from .managers import	 UserManager
# Create your models here.

class User(AbstractUser):
	username = models.CharField(max_length=50,unique=True)
	firstName=models.CharField(max_length=50,null=True,blank=True)
	lastName=models.CharField(max_length=50,null=True,blank=True)
	email = models.EmailField(_('email address'), null=True,blank=True)
	profile = models.ImageField(null=True,blank=True)
	joinDate = models.DateTimeField(auto_now=True)

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = []

	# objects = UserManager()

	def __str__(self):
		return self.username

class BlogPageContent(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	content = models.TextField()
	postDate = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title