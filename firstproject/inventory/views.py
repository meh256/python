from django.shortcuts import render
from django.http import Http404
from inventory.models import item


def index(request):
	items = item.objects.exclude(amount=0)
	return render(request, 'inventory/index.html', {
		'items' : items,
		})

def item_detail(request,id):
	try: 
		litem = item.objects.get(id=id)
	except item.DoesNotExist:
		raise Http404('This Item Does Not Exist')
	return render(request, 'inventory/item_detail.html', {
			'litem' : litem,
		})
