from django.shortcuts import render, redirect
from .models import Grocery

def home(request):
    if request.method == "POST":
        item = request.POST.get("item")
        if item:
            Grocery.objects.create(name=item)

    groceries = Grocery.objects.all()
    return render(request, "grocery/home.html", {"groceries": groceries})

def delete_item(request, id):
    Grocery.objects.get(id=id).delete()
    return redirect("/")