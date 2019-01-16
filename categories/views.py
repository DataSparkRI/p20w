from django.http import HttpResponse
from django.shortcuts import render
from .models import Category
from indicators.models import Indicator

def homepage(request):
	return detail(request, category_slug='home')

def detail(request, category_slug):
	category = Category.objects.get(slug=category_slug)	
	categories = Category.objects.all()
	questions = Indicator.objects.filter(category=category)
	all_questions = Indicator.objects.all()


	popstats = []
	if (category.name == 'Home'):
		is_home = True
		title_element = 'Rhode Island Skills & Jobs Dashboard'
		header_text = 'Rhode Island Skills & Jobs'
		at_a_glance_header = 'Building a talented pipeline.'
		popstats.append({
						'label': 'K-12 Education',
						'stat': '83%',
						'explainer': 'of students graduate high school in 4 years (2016)',
						'link': '/k-12-education'
						}) 
		popstats.append({
						'label': 'Higher Ed',
						'stat': '47%',
						'explainer': 'of working-age RIers hold a postsecondary degree or credential',
						'link': '/higher-education'
						}) 
		popstats.append({
						'label': 'Workforce',
						'stat': '3700+',
						'explainer': 'Served through Real Jobs RI (Sept 2018)',
						'link': '/workforce'
						})  			
	else:
		is_home = False
		title_element = f'{category.name} | Rhode Island Skills & Jobs Dashboard'
		header_text = category.name
		at_a_glance_header = f'Rhode Island {category.at_a_glance_label} at a glance...'
		for q in questions:
			popstats.append({
                               'label': q.pop_stat_label,
                               'stat': q.pop_stat,
                               'explainer': q.pop_stat_explainer,
                            #   'link': f'../deep-dive/{category_slug}/#q{q.id}'
                               'link': f'#q{q.id}'
                           })
	context = {
				'category': category,
                                'category_slug': category_slug,
				'categories': categories,
				'questions': questions,
				'all_questions': all_questions,
				'popstats': popstats,
				'is_home': is_home,
				'title_element': title_element,
				'header_text': header_text,
				'at_a_glance_header': at_a_glance_header, 
				'color_css': f'categories/{category_slug}_color.css',
				}

	return render(request, 'categories/index.html', context)

def deep_dive(request, category_slug):
	
	category = Category.objects.get(slug=category_slug)
#	category = Category.objects.get(slug='deep-dive')	
	categories = Category.objects.all()
	all_questions = Indicator.objects.filter(category=category)

	is_home = False
	title_element = 'Deep Dive | Rhode Island Skills & Jobs Dashboard'
	header_text = category.name + ' - Deep Dive into Data'
	
	context = {
				'category': category,
				'categories': categories,
				'all_questions': all_questions,
				'is_home': is_home,
				'title_element': title_element,
				'header_text': header_text
				}

	return render(request, 'categories/deep_dive.html', context)
	
