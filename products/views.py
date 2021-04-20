from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render

from .forms import ProductModelForm
from .models import Product

# Create your views here.
def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello world</h1>")
    context = {"name": "Georgi"}
    return render(request, "home.html", context)


def search_view(request, *args, **kwargs): # /search/
    # print(args, kwargs)
    # return HttpResponse("<h1>Hello world</h1>")
    query = request.GET.get('q') # q
    qs = Product.objects.filter(title__icontains=query[0])
    print(query, qs)
    context = {"name": "abc", "query": query}
    return render(request, "home.html", context)


def product_detail_view(request, pk):
    try:
        obj = Product.objects.get(pk=pk)
    except  Product.DoesNotExist:
        raise Http404
    # return HttpResponse(f"Product id {obj.pk}")
    return render(request, "products/detail.html", {"object": obj})


def product_list_view(request, *args, **kwargs):
    qs = Product.objects.all()
    context = {"object_list": qs}
    return render(request, "products/list.html", context)


def product_api_detail_view(request, pk, *args, **kwargs):
    try:
        obj = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return JsonResponse({"message": "Not found"})
    return JsonResponse({"id": obj.pk})


@staff_member_required
def product_create_view(request, *args, **kwargs):
    form = ProductModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()

        form = ProductModelForm()
    
    return render(request, "forms.html", {"form": form})

# class HomeView():
#     pass