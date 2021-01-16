from django.db import models

class Person(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30, null=True)

	def toggle_name(self):
		self.last_name, self.first_name = self.first_name, self.last_name
		self.save()
		
		return self.first_name + " " + self.last_name