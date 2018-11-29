from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import Question


class QuestionAdmin(SortableAdminMixin, admin.ModelAdmin):
	list_display = ('name', 'question', 'get_category')
	list_filter = ['category']
	fieldsets = [
		(None, 			{'fields': [('name', 'category'), 'sort_order', 'question', 'text']}), 
		('Dashboard', 	{'fields': ['dashboard_embed', ('aspect_ratio_width', 'aspect_ratio_height')]}), 
		('Pop stat', 	{'fields': ['pop_stat', 'pop_stat_label', 'pop_stat_explainer']})
		]

class QuestionInline(admin.StackedInline):
	model = Question
	extra = 1

admin.site.register(Question, QuestionAdmin)