from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartForm
from django.core.paginator import Paginator


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    paginator = Paginator(products, 6) # this shows 6 products per page
    page = request.GET.get('page')
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        # 'products': paginator.get_page(page),
        'products': products,
    }

    return render(request, 'core/product/list.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form,
    }

    return render(request, 'core/product/detail.html', context)
