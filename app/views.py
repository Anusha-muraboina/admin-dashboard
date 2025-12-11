from django.shortcuts import render

# Create your views here.
# def dashboard(request):
#     return render(request, "dashboard/dashboard.html", {
#         "title": "Dashboard"
#     })

from django.shortcuts import render

def home(request):
    return render(request, 'dashboard/home.html')

def add_user(request):
    return render(request, 'dashboard/add_user.html')

def user_list(request):
    return render(request, 'dashboard/user-list.html')

def roles(request):
    return render(request, 'dashboard/roles.html')

def customers(request):
    return render(request, 'dashboard/customers.html')

def add_product(request):
    return render(request, 'dashboard/add_product.html')

def product_list(request):
    return render(request, 'dashboard/product_list.html')
def pos_page(request):
    return render(request, 'dashboard/pos.html')


def calender(request):
    return render(request, 'dashboard/calender.html')

def updateuser(request):
    return render(request, 'dashboard/update_user.html')