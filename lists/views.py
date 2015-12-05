from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item

def home_page(request):
    if request.method == 'POST':
        next_item_text = request.POST['item_text']
        Item.objects.create(text=next_item_text)
        return redirect('/')
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})
