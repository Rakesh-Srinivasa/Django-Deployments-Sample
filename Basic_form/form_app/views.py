from django.shortcuts import render
from form_app.forms import UserForm
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<em>My Second Project</em>")

def formpage(request):
    #return HttpResponse("<em>from Form Page</em>")
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            
            #print("Validation Success!")
            #print("Name: " + form.cleaned_data['first_name'])
    return render(request,'form_app/form_page.html',{'form':form})
