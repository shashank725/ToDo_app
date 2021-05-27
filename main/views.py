from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from .models import Item, ToDoList
from .forms import CreateNewList

# Create your views here.

def index(response, id):
    ls = ToDoList.objects.get(id=id)
    if response.method == "POST":
        print(response.POST)
        if response.POST.get("save"): #"save" is value of save button
            for item in ls.item_set.all(): #Saving checked Items
                if response.POST.get("c" + str(item.id)) == "clicked": #"clicked" is value of input
                    item.complete = True
                else:
                    item.complete = False
                item.save()
        elif response.POST.get("newItem"):#"newItem" is value of Add Item button
            txt = response.POST.get("new")#"new" is name of the input(Item which going to be added)
            if len(txt) > 2:
                ls.item_set.create(text=txt, complete=False)
            else:
                print("invalid")
    return render(response, "main/list.html", {"ls": ls})

def home(response):
	return render(response, "main/index.html", {'name':'test'})

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
        return HttpResponseRedirect("/%i" %t.id)
    else:
        form = CreateNewList()
    return render(response, "main/create.html", {"form":form})