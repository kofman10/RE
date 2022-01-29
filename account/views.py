from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm

# Create your views here.
def register(request):
    form = SignupForm()
    context = {"regform":form}
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,"index.html",context)