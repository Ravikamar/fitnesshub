from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Category, Product, Order, OrderItem
from django.contrib import messages

def shop_home(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(is_available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/shop_home.html', {
        'category': category,
        'categories': categories,
        'products': products
    })

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_available=True)
    return render(request, 'shop/product_detail.html', {'product': product})

@login_required
def order_create(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        order = Order.objects.create(user=request.user)
        OrderItem.objects.create(order=order, product=product, price=product.price, quantity=1)
        messages.success(request, f'Order for {product.name} has been placed successfully!')
        return redirect('profile')
    return render(request, 'shop/order_confirm.html', {'product': product})
