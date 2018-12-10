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
						'link': '/1'
						}) 
		popstats.append({
						'label': 'Higher Ed',
						'stat': '47%',
						'explainer': 'of working-age RIers hold a postsecondary degree or credential',
						'link': '/2'
						}) 
		popstats.append({
						'label': 'Workforce',
						'stat': '3700+',
						'explainer': 'Served through Real Jobs RI (Sept 2018)',
						'link': '/3'
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
						'link': f'#q{q.id}'				
					})
	context = {
				'category': category,
				'categories': categories,
				'questions': questions,
				'popstats': popstats,

				'is_home': is_home,
				'title_element': title_element,
				'header_text': header_text,
				'at_a_glance_header': at_a_glance_header
				}
	return render(request, 'categories/index.html', context)
