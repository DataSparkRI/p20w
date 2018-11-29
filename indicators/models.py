from django.db import models
from tinymce.models import HTMLField

class Question(models.Model):
	name = models.CharField(max_length=20, help_text='Reference for internal use only. Does not display.')
	question = models.CharField(max_length=200, help_text='I.E. What career education programs are available to students?')
	text = HTMLField(help_text='Explanatory text.')

	category = models.ForeignKey('categories.Category', on_delete=models.PROTECT)
	sort_order = models.PositiveSmallIntegerField(default=0)

	dashboard_embed = models.TextField(help_text='Embed code from PowerBI')
	aspect_ratio_width = models.PositiveSmallIntegerField(default=16, help_text='Defaults to 16x9')
	aspect_ratio_height = models.PositiveSmallIntegerField(default=9, help_text='Defaults to 16x9')

	pop_stat = models.CharField(max_length=5, help_text='Number that displays in the pop-stat at the top of the screen. Include %$ etc. 5 character max')
	pop_stat_label = models.CharField(max_length=12, help_text='Label at the top of the pop-stat. 12 character max.')
	pop_stat_explainer = models.CharField(max_length=60, help_text='Explainer under the pop-stat. 60 character max.')

	def __str__(self):
		return f'{self.category.name} - {self.name}'

	class Meta:
		ordering = ['sort_order']

	def get_category(self):
		return self.category.name 
