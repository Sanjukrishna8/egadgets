from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
router=DefaultRouter()
router.register("prod",productVset,basename="prod")
router.register("productmv",productMVSet,basename="pmv")
router.register("user",UserVSet,basename="us")

urlpatterns=[
    path('product',productView.as_view()),
    path('product/<int:id>',SpecificProductView.as_view()),
    path('token',views.obtain_auth_token)
]+router.urls