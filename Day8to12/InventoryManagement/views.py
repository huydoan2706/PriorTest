from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Inventory, Receipt
from .forms import CreateNewReceipt
# Create your views here.


def index(request, id):
    receipt = Receipt.objects.get(id=id)

    if receipt in request.user.receipt.all():
        if request.method == 'POST':
            print(request.POST)
            if request.POST.get("save"):
                for item in receipt.inventory_set.all():
                    item.name = request.POST.get("N"+str(item.id))
                    item.quantity = request.POST.get("Q"+str(item.id))
                    item.type = request.POST.get("T"+str(item.id))
                    item.brand = request.POST.get("B"+str(item.id))
                    item.price = request.POST.get("P"+str(item.id))
                    item.save()

            elif request.POST.get("newInventory"):
                name = request.POST.get("new")
                if 2 < len(name) <= 100:
                    receipt.inventory_set.create(name=name, quantity=1)
                else:
                    print("invalid")

        return render(request, 'InventoryManagement/receipt.html', {"receipt": receipt})
    return render(request, 'InventoryManagement/view.html', {})

def home(request):
    return render(request, 'InventoryManagement/home.html', {})


def create(request):
    if request.method == "POST":
        form = CreateNewReceipt(request.POST)
        r = None
        if form.is_valid():
            supplier_name = form.cleaned_data.get("supplier_name")
            r = Receipt(supplier_name=supplier_name)
            r.save()
            request.user.receipt.add(r)
        receipt_list = list(Receipt.objects.all())
        id = Receipt.objects.get(id=len(receipt_list)).id
        return HttpResponseRedirect("/%i" % id)

    else:
        form = CreateNewReceipt()

    return render(request, 'InventoryManagement/create.html', {"form": form})


def view(request):
    return render(request, 'InventoryManagement/view.html', {})
