from django.shortcuts import render, redirect
from .models import Store
from .forms import StoreForm

def store_list(request):
    stores = Store.objects.all()
    return render(request, 'stores/store_list.html', {'stores': stores})


from django.http import Http404
def store_detail(request, pk):
    try:
        store = Store.objects.get(pk=pk)
    except Store.DoesNotExist:
        raise Http404
    return render(request, 'stores/store_detail.html', {'store': store})

def store_create(request):
    if request.method == 'POST':
        form = StoreForm(request.POST, submit_title='建立')   # 注意這行
        if form.is_valid():
            store = form.save()
            return redirect(store.get_absolute_url())
    else:
        form = StoreForm(submit_title='建立')                 # 注意這行
    return render(request, 'stores/store_create.html', {'form': form})


def store_update(request, pk):
    try:
        store = Store.objects.get(pk=pk)
    except Store.DoesNotExist:
        raise Http404
    if request.method == 'POST':
        # 注意這行
        form = StoreForm(request.POST, instance=store, submit_title='更新')
        if form.is_valid():
            store = form.save()
            return redirect(store.get_absolute_url())
    else:
        # 注意這行
        form = StoreForm(instance=store, submit_title='更新')
    return render(request, 'stores/store_update.html', {
        'form': form, 'store': store,
    })