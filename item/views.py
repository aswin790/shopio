from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from . models import item,category
from . forms import NewItemForm,EditItemForm
# Create your views here.



def search_items(request):
    query = request.GET.get('query','')
    categories = category.objects.all()
    category_input = request.GET.get('category',0)
    items = item.objects.filter(is_sold = False)

    if query:
        items = items.filter(Q(name__icontains = query) | Q(description__icontains = query))

    if category_input:
        items = items.filter(category = category_input )   

    return render(request,'core/index.html',{
        'items':items,
        'query':query,
        'categories':categories,
        'category_id':int(category_input)
        })


def details(request,pk):
    print("jo")
    item_instance = get_object_or_404(item,pk=pk)
    related_items = item.objects.filter(category = item_instance.category ,is_sold = False).exclude(pk = pk)[0:4]

    return render(request,'details.html',{
        'item_instance':item_instance,
        'related_items':related_items,
        })
@login_required
def new_item(request):
    if request.POST:
        form_obj = NewItemForm(request.POST,request.FILES)
        if form_obj.is_valid():
            print(request.FILES)
            obj = form_obj.save(commit=False)
            obj.created_by = request.user
            obj.save()
            
            return redirect('Item:details',pk = obj.id)
    else:
        form = NewItemForm()

    return render(request,'user/new_item_form.html',{'form':form})

@login_required
def item_delete(request,pk):
    item.objects.get(pk=pk).delete()
    return redirect('/')

@login_required
def item_edit(request,pk):
    my_item = get_object_or_404(item,pk= pk,created_by = request.user)
    if request.POST:
        form_obj = EditItemForm(request.POST,request.FILES,instance=my_item)
        if form_obj.is_valid():
            form_obj.save()
            
            return redirect('Item:details',pk = pk)
    else:
        form = EditItemForm(instance=my_item)

    return render(request,'user/new_item_form.html',{'form':form})


            




