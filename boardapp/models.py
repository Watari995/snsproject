from django.db import models

class BoardModel(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField()
  author = models.CharField(max_length=50)
  snsimage = models.ImageField(upload_to='')
  good = models.IntegerField(null=True, blank=True, default=1)
  read = models.IntegerField(null=True, blank=True, default=1)
  readtext = models.TextField(null=True, blank=True, default='a')

  def __str__(self):
    return self.title