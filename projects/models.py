from django.db import models


class Language(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Project(models.Model):
	name = models.CharField(max_length=100)
	short_summary = models.CharField(max_length=250)
	description = models.TextField()
	languages_used = models.ManyToManyField('Language', blank=True)
	cover_image = models.ImageField(upload_to='project_images/')
	repository_link = models.URLField(null=True, blank=True)
	live_demo_link = models.URLField(null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True)
	featured = models.BooleanField(default=False)
	is_public = models.BooleanField(default=True)

	def __str__(self):
		return self.name