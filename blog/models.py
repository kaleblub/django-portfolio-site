from django.db import models
from django.utils import timezone

class Tag(models.Model):
	name = models.CharField(max_length=50, unique=True)

	def __str__(self):
		return self.name

class Post(models.Model):
	title = models.CharField(max_length=100)
	summary = models.CharField(max_length=100)
	tags = models.ManyToManyField(Tag)
	author = models.CharField(max_length=20, default="Kaleb Humpal")
	date_posted = models.DateTimeField(default=timezone.now)
	content = models.TextField()

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})