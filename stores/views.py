from django.shortcuts import render, redirect
from .models import Shop, Item
from .forms import ShopForm, ItemForm

# Create your views here.
def shop_list(request):
    shops = Shop.objects.all()

    context = {
        "shops":shops
    }

    return render(request, "shop_list.html", context)

def shop_create(request):
    form = ShopForm()
    if request.method =="POST":
        form = ShopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shop-list')
    context = {
        "form":form
    }
    return render(request, 'create_shop.html', context)


def item_list(request):
    items = Item.objects.all()

    context = {
        "items":items
    }

    return render(request, "item_list.html", context)

def item_create(request):
    form = ItemForm()
    if request.method =="POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item-list')
    context = {
        "form":form
    }
    return render(request, 'create_item.html', context)

def item_update(request, item_id):
    item_obj = Item.objects.get(id=item_id)
    form = ItemForm(instance=item_obj)
    if request.method == "POST":
            form = ItemForm(request.POST, instance=item_obj)
            if form.is_valid():
                form.save()
                return redirect('item-list')
    context = {
            "item_obj": item_obj,
            "form":form,
        }
    return render(request, 'update.html', context)




