from django.contrib import auth
from django.shortcuts import render, redirect
from .forms import CompanyForm, MaterialsFormset
from .models import Company, User


# function to add company wise agent names
def register(request):
    context = {}
    if request.method == 'POST':  # getting values from the user
        form = CompanyForm(request.POST)
        if form.is_valid():  # checking validation
            co_obj = form.save()  # saving values into an object
            formset = MaterialsFormset(request.POST, instance=co_obj)  # sending the parent class details as instance
            if formset.is_valid():
                formset.save()  # saving the child class details
                return redirect('login')  # once data added sending to login page
    else:
        context['form'] = CompanyForm()
        context['formset'] = MaterialsFormset()
        return render(request, 'register.html', context)  # if no data added remain on same page


# creating login page
def login(request):
    if request.method == 'POST':
        username1 = request.POST['uname']  # getting values entered by the user
        password1 = request.POST['psw']
        x = auth.authenticate(username=username1, password=password1)  # validating
        if x is None:
            context = {'msg': 'Invalid username or password'}  # msg to be shown if failed
            return render(request, 'login.html', context)  # to the login page
        else:
            return redirect('dash')  # correct credentials given will take the user to the dashboard
    else:
        return render(request, 'login.html')  # not getting any value will remain on same page


# dashboard where all the functions will be available
def dash(request):
    company_object = Company.objects.all()  # getting all company in  a object
    return render(request, 'dash.html', {'company_object': company_object})  # sending to dashboard


# creating user function to show user detail fo a perticular company using id
def userlist(request, id=None):
    com = Company.objects.get(pk=id)  # getting detail of company in com object
    user_list = com.user_set.all()  # object holding user list
    return render(request, 'userlist.html', {"user_list": user_list})  # sending values to user list page
