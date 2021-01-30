from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class Assignment(models.Model):
	CHOICES =(
    ('pending','pending'),
    ('under_revision', 'under_revision'),
    ('completed', 'comleted')
	)
	order_file = models.FileField(upload_to='assignments')
	title = models.CharField(max_length=150)
	topic =models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	time_due = models.DateTimeField(default=timezone.now)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	status = models.CharField(default=CHOICES[0], choices=CHOICES, max_length=50)
	final_work = models.FileField(upload_to='final_work_file',blank=True, null=True)

	def __str__(self):
		self.title

	def get_absolute_url(self):
		return reverse('a-detail', kwargs={'pk':self.pk})

class Order(models.Model):
	CHOICES =(
    ('pending','pending'),
	('under_review', 'under_review'),
    ('under_revision', 'under_revision'),
	('canceled', 'canceled'),
    ('completed', 'comleted')
	)
	order_file = models.FileField(upload_to='media')
	title = models.CharField(max_length=150)
	topic = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	due_time = models.DateTimeField(default=timezone.now)
	user_assigned = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	status = models.CharField(default=CHOICES[0], choices=CHOICES, max_length=50)
	file_upload = models.FileField(upload_to='final_files',blank=True, null=True)

	def __str__(self):
		return self.title



'''class Final_copy(models.Model):
	order = models.ForeignKey(Order, on_delete=models.CASCADE)
	file_to_submit = models.FileField(upload_to='order_submission')
	complete = models.BooleanField()

	
	def __str__(self):
		return self.order

'''

		




