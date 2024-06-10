from django.contrib.auth.decorators import login_required

from django.shortcuts import render, get_object_or_404, redirect # type: ignore
from .models import Item

from .forms import NewItemForm, EditItemForm

# https://youtu.be/ZxMB6Njs3ck?t=2762

# Create your views here.
def items(request): #for the search or browse function
    query = request.GET.get('query', '') #https://youtu.be/ZxMB6Njs3ck?t=6370 - Backend for the equery function
    items = Item.objects.filter(is_sold=False)

    return render(request, 'item/browse.html', {'items': items, 'query': query})


def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=item.pk)

    return render(request, 'item/details.html', {'item':item, 'related_items':related_items})


@login_required #Ensures user is login, else redirects user to login page
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES) #request.FILES enables us to get the Files(images in this case) from the form

        if form.is_valid():
            item = form.save(commit=False) #we dont save immediately bcus it won't add creaed_by, so it would raise an error
            item.created_by = request.user #so we manually add the created_by 
            item.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemForm()

    return render(request, 'item/form.html', {'form': form ,'title': 'New Item' })


@login_required #Ensures user is login, else redirects user to login page
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item) #https://youtu.be/ZxMB6Njs3ck?t=5947

        if form.is_valid():
            form.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item) #the "instance=item" passes the values into the edit form

    return render(request, 'item/form.html', {'form': form ,'title': 'New Item' })

@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    item.delete()

    return redirect('dashboard:index')