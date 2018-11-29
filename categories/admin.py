from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from categories.models import Category


class CategoryAdmin(SortableAdminMixin, admin.ModelAdmin):
	pass


admin.site.register(Category, CategoryAdmin)