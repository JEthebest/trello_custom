from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import OrderCardForm

# Create your views here.

def order_create(request):
    form = OrderCardForm(request.POST or None)
    context = {}
    context['order_form'] = form
    return render(request, 'order_create.html', context)

def order_save(request):
    if request.method == 'POST':
        form = OrderCardForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            return redirect('board:home')