from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,FormView
from .forms import RegForm,LogForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
# Create your views here.

class LogView(FormView):
    template_name="log.html"
    form_class=LogForm
    def post(self,request):
        fdata=LogForm(data=request.POST)
        if fdata.is_valid():
            uname=fdata.cleaned_data.get("username")
            pswd=fdata.cleaned_data.get("password")
            user=authenticate(request,username=uname,password=pswd)
            if user:
                login(request,user)
                return redirect("ch")
            else:
                return render(request,"log.html",{"form":fdata})



# class LogView(View):
#     def get(self,request):
#         form=LogForm()
#         return render(request,"log.html",{'form':form})
#     def post(self,request):
#         fdata=LogForm(data=request.POST)
#         if fdata.is_valid():
#             uname=fdata.cleaned_data.get("username")
#             pswd=fdata.cleaned_data.get("password")
#             user=authenticate(request,username=uname,password=pswd)
#             if user:
#                 login(request,user)
#                 return redirect("ch")
#             else:
#                 return render(request,"log.html",{"form",fdata})
    
# class RegView(View):
#     def get(self,request):
#         form=RegForm()
#         return render(request,"reg.html",{"form":form})
#     def post(self,request):
#         fdata=RegForm(data=request.POST)
#         if fdata.is_valid():
#             fdata.save()
#             return redirect("log")
#         else:
#             return render(request,"reg.html",{"form":fdata})

class RegView(CreateView):
    template_name="reg.html"
    form_class=RegForm
    success_url=reverse_lazy("log")


class lgOut(View):
    def get(self,request):
        logout(request)
        return redirect("log")