from django.db import models

# Create your models here.
from django.urls import reverse

class News(models.Model):
	title = models.CharField(max_length=300)
	published_at = models.CharField(max_length=300)
	author = models.CharField(max_length=300)
	desciption = models.CharField(max_length=300)
	url = models.CharField(max_length=300)
	url_to_image = models.CharField(max_length=300)
	content = models.CharField(max_length=300)
	source = models.CharField(max_length=300)

	

	def __str__(self):
		return self.title


	def get_absolute_url(self):
		return reverse('note_detail', args=[str(self.id)])
