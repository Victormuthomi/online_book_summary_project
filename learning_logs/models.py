from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
	"""A class thats stores the topic a user is learning"""
	text = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	
	def __str__(self):
		"""return a string representation of the model"""
		return self.text
		
class Entry(models.Model):
	"""something specific learned in a topic"""
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
	text = models.TextField()
	added_date = models.DateTimeField(auto_now_add=True)
	
	
	class Meta():
		verbose_name_plural = 'enteries'
	
	def __str__(self):
		"""return a string represntation of the model"""
		if len(self.text) > 50:
			return self.text[:50] + '...'
		else:
			return self.text[:50]
		
	
