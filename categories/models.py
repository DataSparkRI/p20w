from django.db import models
from tinymce.models import HTMLField
from django.utils.text import slugify

class Category(models.Model):
	name = models.CharField(max_length=50)
	slug = models.SlugField(unique=True, null=True, blank=True, help_text="auto fill if it is blank")
	navigation_name = models.CharField(max_length=20)
	# homepage_image = models.ImageField()
	category_page_image = models.ImageField(upload_to='category_headers')
	category_page_image_offset = models.IntegerField(default=50, help_text='Percent from top to offset the header image.')
	intro_header = models.CharField(max_length=200)
	intro_text = HTMLField()
	at_a_glance_label = models.CharField(max_length=30, help_text='Rhode Island ??? at a glance')
    
	def save(self, *args, **kwargs):
		if self.slug == None:
		   self.slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)
    
	class Meta:
		verbose_name_plural = 'categories'

	def __str__(self):
		return self.name