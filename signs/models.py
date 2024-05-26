from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'categories'

    def __str__(self):
        return self.name

class RoadSigns(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/roadsign',blank=True,null=True)
    video = models.FileField(upload_to='videos',blank=True,null=True)
    audio = models.FileField(upload_to='audio',blank=True,null=True)

    class Meta:
        db_table = 'roadsigns'

    def __str__(self):
        return self.name