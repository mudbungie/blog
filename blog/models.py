from django.db import models

class Category(models.Model):
	title = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(max_length=100, unique=True)

	def get_absolute_url(self):
		return '/category/{}'.format(self.slug)

class Post(models.Model):
	title = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(max_length=100, unique=True)
	body = models.TextField()
	posted = models.DateTimeField(db_index=True, auto_now_add=True)
	category = models.ForeignKey('blog.Category')

	def get_absolute_url(self):
		return '/post/{}'.format(self.slug)
