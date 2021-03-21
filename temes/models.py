from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=225, unique=True, default="")
    link_teoria = models.CharField(max_length=225, null=True)
    # slug = models.SlugField(blank=True, default='')

    def __str__(self):
        return self.title
    #
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super(Category, self).save()
    #
    # def get_absolute_url(self):  # < here
    #     return reverse('detail', args=[str(self.slug)])

class Exercici(models.Model):
    exercici = models.IntegerField()
    any = models.CharField(max_length=20)
    imatge = models.CharField(max_length=200)
    sol_a = models.CharField(max_length=60, blank=True, null=True)
    sol_b = models.CharField(max_length=60, blank=True, null=True)
    sol_c = models.CharField(max_length=60, blank=True, null=True)
    sol_d = models.CharField(max_length=60, blank=True, null=True)
    sol_e = models.CharField(max_length=60, blank=True, null=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.PROTECT)