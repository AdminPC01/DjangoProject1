from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import ToDoList,Item
from .forms import CreateNewList
# Create your views here.

def list(response,id):
    ls = ToDoList.objects.get(id=id)

    if ls in response.user.todolist.all():

        if response.method == "POST":
            if response.POST.get("save"):
                for item in ls.item_set.all():
                    if response.POST.get("c" + str(item.id)) == "clicked":
                        item.complete = True
                    else:
                        item.complete = False

                    item.save()

            elif response.POST.get("newItem"):
                txt = response.POST.get("new")

                if len(txt) > 2:
                    ls.item_set.create(text=txt, complete=False)
                else:
                    print("invalid")
            return render(response, "main/list.html", {"ls": ls})

    return render(response, "main/home.html", {})
def base(response):
    return render(response,"main/create.html",{})

def home(response):
    return render(response,"main/home.html",{})

def create(response):
    form = CreateNewList(response.POST or None)
    if (response.method == "POST"): # we are trying passing some information from our form page to this page
       form = CreateNewList(response.POST)  # it's going to contain all attributes, information about object
       if(form.is_valid()):
            n = form.cleaned_data["name"] # we are getting all data from form
            t = ToDoList(name=n) # Name from form passes into the list
            t.save()
            response.user.todolist_set.create(name = n)
            return HttpResponseRedirect("/%i" %t .id)
       else:
        form = CreateNewList()
    return render(response, "main/create.html", {"form": form})

def view (response):
    return  render(response,"main/view.html", {})