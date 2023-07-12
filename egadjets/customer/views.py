from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView,ListView,DetailView
from store.models import product
from .models import Cart,Order
from django.contrib import messages
from django.db.models import Sum
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
#auth_decorator

def signin_required(fn):
    def inner(request,*args,**kwargs):
        if request.user.is_authenticated:
           return fn(request,*args,**kwargs)
        else:
            messages.error(request,"please Login first")
            return redirect("log")
    return inner
dec=[signin_required,never_cache]
# Create your views here.
@method_decorator(dec,name="dispatch")
class CustHomeView(ListView):
    template_name="cust-home.html"
    model=product
    context_object_name="data"

@method_decorator(dec,name="dispatch")
class ProductDetailView(DetailView):
    template_name="product-details.html"
    model=product
    context_object_name="product"
    pk_url_kwarg="pid"

dec
def addcart(request,pid):
    prod=product.objects.get(id=pid)
    user=request.user
    Cart.objects.create(product=prod,user=user)
    messages.success(request,"product Added To cart")
    return redirect("ch")

@method_decorator(dec,name="dispatch")
class CartListView(ListView):
    template_name="cart-list.html"
    model=Cart
    context_object_name="cartitem"

    def get_queryset(self):
        cart=Cart.objects.filter(user=self.request.user,status="cart")
        total=Cart.objects.filter(user=self.request.user,status='cart').aggregate(tot=Sum("product__price"))
        return {"items":cart,"total":total}
    # filter is used to override  

dec
def DeleteCartitem(request,id):
   cart=Cart.objects.get(id=id)
   cart.delete()
   messages.error(request,"cart item removed")
   return redirect("vcart")


@method_decorator(dec,name="dispatch")
class CheckoutView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"checkout.html")
    def post(self,request,*args,**kwargs):
         id=kwargs.get("cid")
         cart=Cart.objects.get(id=id)
         prod=cart.product
         user=request.user
         address=request.POST.get("address")
         phone=request.POST.get("phone")
         Order.objects.create(product=prod,user=user,address=address,phone=phone)
         cart.status="order placed"
         cart.save()
         messages.success(request,"order placed successfully")
         return redirect("ch")
    
@method_decorator(dec,name="dispatch")   
class OrderView(ListView):
    template_name="orders.html"
    model= Order
    context_object_name="order"
    def get_queryset(self):
        order=Order.objects.filter(user=self.request.user)
        return {"order":order}
    
dec   
def cancel_order(request,id):
    order=Order.objects.get(id=id)
    order.status="cancel"
    order.save()
    messages.success(request,"order Cancelled")
    return redirect("order")