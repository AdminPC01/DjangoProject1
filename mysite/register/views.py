from django.shortcuts import render, redirect
from .forms import RegisterForm
# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/home")
    else:
        form = RegisterForm()
    return render(response, "register/register.html", {"form": form})
    #
    #   {%if user.is_authenticated%}
    # {% block content %}
    # <h1>Base page</h1>
    # {% endblock %}
    #  {%else%}
    #           <p>Login <a href="/login/login"> here</a> </p>
    #           {%endif%}