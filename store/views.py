from django.shortcuts import render, redirect, get_object_or_404

from .forms import ProductForm
from .models import Product


def index(request):
    context = {}
    context['products_for_sale'] = Product.objects.filter(sold_to=None)
    if request.user.is_authenticated:
        context['bought_products'] = request.user.purchases.all()
        context['products_for_sale'] = context['products_for_sale'].exclude(owner=request.user)
    return render(request, "product/index.html", context)


def detail(request, product_id):
    context = {'product': Product.objects.get(id=product_id)}
    return render(request, "product/detail.html", context)


def product_new(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.owner = request.user
            product.save()
            context = {'product': product}
            return render(request, "product/detail.html", context)
    else:
        form = ProductForm()
    return render(request, 'product/product_edit.html', {'form': form})


def user_products(request):
    if request.user.is_authenticated:
        products_list = request.user.product_set.all()
        context = {'products_list': products_list}
        return render(request, 'product/user_products.html', context)
    else:
        return redirect('/accounts/login/')


def buy(request, product_id):
    product = Product.objects.get(id=product_id)
    product.sold_to = request.user
    product.save()
    return redirect('/store/')


def delete(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('/store/myproducts')
    return render(request, 'product/confirm_delelte.html', {'product': product})

