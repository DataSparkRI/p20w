from django.contrib import admin

from .models import Indicator, Question

class QuestionAdmin(admin.ModelAdmin):
	list_display = ('name', 'question', 'get_indicator', 'get_category')
	list_filter = ['indicator__category', 'indicator']
	fieldsets = [
		(None, 			{'fields': [('name', 'indicator'), 'question', 'text']}), 
		('Dashboard', 	{'fields': ['dashboard_embed', ('aspect_ratio_width', 'aspect_ratio_height')]}), 
		('Pop stat', 	{'fields': ['pop_stat', 'pop_stat_label', 'pop_stat_explainer']})
		]

class QuestionInline(admin.StackedInline):
	model = Question
	extra = 1

class IndicatorAdmin(admin.ModelAdmin):
	fields = ['category', 'name']
	inlines = [QuestionInline] 


admin.site.register(Indicator, IndicatorAdmin)
admin.site.register(Question, QuestionAdmin)