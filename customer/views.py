from django.shortcuts import render
from django.views import View

from django.core.mail import send_mail
from django.db.models import Q

from .models import MenuItem, Category, OrderModel
from django.db import IntegrityError

def index(request):
	return render(request, 'customer/index.html')

def about(request):
	return render(request, 'customer/about.html')


#def order(request):
#	currys = MenuItem.objects.filter(category__name__contains='Curry')
#	deserts = MenuItem.objects.filter(category__name__contains='Desert')
#	drinks = MenuItem.objects.filter(category__name__contains='Drink')

#	order_items = {
#		'items':[],
#	}

#	items = request.POST.getlist('items[ ]')

#	for item in items:
#		menu_item = MenuItem.object.get(pk__contains=int(item))
#		item_data = {
#			'id': menu_item.pk,
#			'name': menu_item.name,
#			'price': menu_item.price
#		}

#		order_items['items'].append(item_data)

#	price = 0
#	item_ids = []

#	for item in order_items['items']:
#		price += item['price']
#		item_ids.append(item['id'])

#	order = OrderModel.objects.create(price=price)
#	order.items.add(*item_ids)

	
	#return render (request, 'customer/order_confirmation')

#	context = {
#		'currys':currys,
#		'deserts':deserts,
#		'drinks':drinks,
#		'items': order_items['items'],
#		'price': price,
#	}

#	return render(request, 'customer/order.html', context)

class order(View):
	def get(self, request, *args, **kwargs):
		currys = MenuItem.objects.filter(category__name__contains='Curry')
		deserts = MenuItem.objects.filter(category__name__contains='Desert')
		drinks = MenuItem.objects.filter(category__name__contains='Drink')

		#return render (request, 'customer/order_confirmation')

		context = {
			'currys':currys,
			'deserts':deserts,
			'drinks':drinks,
		}

		return render(request, 'customer/order.html', context)

	def post(self, request, *args, **kwargs):
		name = request.POST.get('name')
		email = request.POST.get('email')
		phone = request.POST.get('phone')
		street = request.POST.get('street')
		city = request.POST.get('city')

		order_items = {
			'items':[],
		}

		items = request.POST.getlist('items[]')

		for item in items:
			menu_item = MenuItem.objects.get(pk__contains=int(item))
			item_data = {
				'id': menu_item.pk,
				'name': menu_item.name,
				'price': menu_item.price,
			}

			order_items['items'].append(item_data)

			price = 0
			item_ids = []

		for item in order_items['items']:
			price += item['price']
			item_ids.append(item['id'])

		order = OrderModel.objects.create(
				price=price,
				name=name,
				email = email,
				phone = phone,
				street = street,
				city = city,
				)

		order.items.add(*item_ids)

		body = ('Thank You For Your Order! Your Food is being made and will be delivered soon!\n'
			f'Your Total: {price}\n'
			'Thank you again for your order!')

		send_mail(
			'Thank You For Your Order!',
			body,
			'example@example.com',
			[email],
			fail_silently=False
			)

		context = {
			'items': order_items['items'],
			'price': price,
		}

		return render(request, 'customer/order_confirmation.html', context)


class Menu(View):
	def get(self, request, *args, **kwargs):
		menu_items = MenuItem.objects.all()

		context = {
			'menu_items':menu_items
		}

		return render(request, 'customer/menu.html', context)

class MenuSearch(View):
	def get(self, request, *args, **kwargs):
		query = self.request.GET.get("q")

		menu_items = MenuItem.objects.filter(
			Q(name__icontains=query) |
			Q(price__icontains=query) |
			Q(description__icontains=query) 
			)

		context = {
			'menu_items':menu_items
		}

		return render(request, 'customer/menu.html', context)
