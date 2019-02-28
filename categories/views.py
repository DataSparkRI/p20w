from django.http import HttpResponse
from django.shortcuts import render
from .models import Category
from indicators.models import Indicator

def home_page(request):
	return page(request, category_slug='home', page_type='home')

def category_page(request, category_slug):
	return page(request=request, category_slug=category_slug, page_type='category')

def deepdive_page(request, category_slug):
	return page(request=request, category_slug=category_slug, page_type='deepdive')

def page(request, category_slug, page_type):
	category = Category.objects.get(slug=category_slug)	
	categories = Category.objects.all()
	indicators = Indicator.objects.filter(category=category)

	popstats = []
	hp_popstat_colors = []
	if (page_type == 'home'):
		title_element = 'Rhode Island Skills & Jobs Dashboard'
		header_text = 'Rhode Island Skills & Jobs'
		at_a_glance_header = 'Building a talented pipeline.'
		hp_popstats = Category.objects.exclude(name='Home')
		for hp_popstat in hp_popstats: 
			popstats.append({
							'label': hp_popstat.navigation_name,
							'stat': hp_popstat.homepage_pop_stat,
							'explainer': hp_popstat.homepage_pop_stat_explainer,
							'link': '/' + hp_popstat.slug,
							'icon': hp_popstat.homepage_pop_stat_icon,
							'class': hp_popstat.slug
			})
			hp_popstat_colors.append({
							'class': hp_popstat.slug,
							'color': hp_popstat.color,
							'color_light': hp_popstat.color_light,
							'color_lightest': hp_popstat.color_lightest,
			})
		
	elif (page_type == 'category'):
		title_element = f'{category.name} | Rhode Island Skills & Jobs Dashboard'
		header_text = category.name
		at_a_glance_header = f'Rhode Island {category.at_a_glance_label} at a glance...'
		for indicator in indicators:
			popstats.append({
                               'label': indicator.pop_stat_label,
                               'stat': indicator.pop_stat,
                               'explainer': indicator.pop_stat_explainer,
                               'link': f'#q{indicator.id}'
                           })
	elif (page_type == 'deepdive'):
		title_element = f'{category.name} | Deep Dive into Data | Rhode Island Skills & Jobs Dashboard'
		header_text = category.name
		category.intro_header = 'Deep Dive Into Data'
		at_a_glance_header = ''

	context = {
				'category': category,
                'category_slug': category_slug,
				'categories': categories,
				'indicators': indicators,
				'popstats': popstats,
				'hp_popstat_colors': hp_popstat_colors,
				'page_type': page_type,
				'title_element': title_element,
				'header_text': header_text,
				'at_a_glance_header': at_a_glance_header, 
				}

	return render(request, 'categories/index.html', context)
