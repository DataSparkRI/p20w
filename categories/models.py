from django.db import models
from tinymce.models import HTMLField
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, null=True,
                            blank=True, help_text="auto fill if it is blank")
    navigation_name = models.CharField(max_length=20)
    category_page_image = models.ImageField(upload_to='category_headers')
    category_page_image_offset = models.IntegerField(
        default=50, help_text='Percent from top to offset the header image.')
    intro_header = models.CharField(max_length=200)
    description = HTMLField()
    narrative_text = HTMLField(null=True, blank=True)
    at_a_glance_label = models.CharField(
        max_length=30, help_text='Rhode Island ??? at a glance')
    agency_url = models.URLField(
        max_length=100, null=True, blank=True, help_text='Agency URL')
    sort_order = models.PositiveSmallIntegerField(default=0)
    color = models.CharField(max_length=20, default='steelblue')
    color_light = models.CharField(max_length=20, default='lightsteelblue')
    color_lightest = models.CharField(max_length=20, default='#DDDDEE')
    info_graphic = models.FileField(
        upload_to='infographics', null=True, blank=True)
    homepage_pop_stat = models.CharField(max_length=5, blank=True, null=True,
                                         help_text='Number that displays in the pop-stat at the top of the screen. Include %$ etc. 5 character max')
    homepage_pop_stat_explainer = models.CharField(
        max_length=60, blank=True, null=True, help_text='Explainer under the pop-stat. 60 character max.')
    homepage_pop_stat_icon = models.CharField(
        max_length=20, blank=True, null=True, help_text='Icon class from fontawesome for the icon that appears when you hover over the popstat. ')

    def save(self, *args, **kwargs):
        if self.slug == None:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        ordering = ['sort_order']
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
