from django.shortcuts import render
from django.views.generic import DetailView

from Shop.models import Product


# Create your views here.

def show_index_page(request):
    context = {'products': Product.objects.all()}
    return render(request, 'Shop/index.html', context=context)


class DetailViewPage(DetailView):
    model = Product
    template_name = 'Shop/detail.html'
    pk_url_kwarg = 'product_id'
    context_object_name = 'product'
