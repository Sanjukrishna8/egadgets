from django.urls import path
from .views import *

urlpatterns=[
    path('chome',CustHomeView.as_view(),name='ch'),
    path('prodet/<int:pid>',ProductDetailView.as_view(),name='pdet'),
    path('acart/<int:pid>',addcart,name='acart'),
    path('viewcart',CartListView.as_view(),name='vcart'),
    path('delcart/<int:id>',DeleteCartitem,name="dcart"),
    path('check/<int:cid>',CheckoutView.as_view(),name="checkout"),
    path('orders',OrderView.as_view(),name='order'),
    path('cancelorder/<int:id>',cancel_order,name='orderc')
]