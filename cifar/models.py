from django.db import models


class ImageClassificationResult(models.Model):
	image = models.ImageField(upload_to='images/%Y/%m/%d/')
	result = models.CharField(max_length=100, null=True)
