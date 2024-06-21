from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from salama.models import OrderForm, salama_register
from salama.forms import register_form, UserRegistrationForm, UserLoginForm, Salama_OrderForm
from django.contrib.auth.decorators import login_required


def home(request):
    stored_messages = messages.get_messages(request)
    return render(request, 'index.html', {'messages': stored_messages})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')

# def register(request):
#     if request.method == 'POST':
#         form = register_form(request.POST) 
#         if form.is_valid():
#             form.save()
#             messages.success(request,
#                              'Registratoion successful! Welcome to Salama Millers ltd.!')
#             return redirect('handlesignup')
#     else:
#         form = register_form()
#         return render(request, 'customerregister.html', {'form': form})


def handlesignup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,
                             'Account created successfully! Welcome!')
            return redirect('handlelogin')
        else:
            return render(request, 'customersignup.html', {'form': form})
    else:
        form = UserRegistrationForm()
        return render(request, 'customersignup.html', {'form': form})


def handlelogin(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Login successful! Welcome, {username}! ')
                return redirect('home')  # Redirect to the home page after successful login
            else:
                messages.error(request, 'Invalid username or password. Please try again.')
    else:
        form = UserLoginForm()
    return render(request, 'customerlogin.html', {'form': form})


def handlelogout(request):
    logout(request)
    return redirect('home')



@login_required
def create_order(request):
    if request.method == 'POST':
        item = request.POST.get('item')
        description = request.POST.get('description')
        quantity = request.POST.get('quantity')

        # creating a new order and associating it with the logged-in user/customer

        new_order = OrderForm.objects.create(
            item=item,
            description=description,
            quantity=quantity,
            user=request.user  # linking the order with the logged-in user/customer
        )

        messages.success(request,
                         'Order successful! We shall inform you once processed. Thank you for shopping with us!')
        return redirect('view_orders')
    else:
        return render(request, 'order.html')

def view_orders(request):
    data = OrderForm.objects.filter(user=request.user)
    return render(request, 'view_orders.html', {'data': data})


def edit(request, id):
    order = OrderForm.objects.get(id=id)
    return render(request, 'edit.html', {'order': order})

def updateData(request, id):
    if request.method == 'POST':
        item = request.POST.get('item')
        description = request.POST.get('description')
        quantity = request.POST.get('quantity')
        route = request.POST.get('route')

        rekebisha = OrderForm.objects.get(id=id)
        rekebisha.item = item
        rekebisha.description = description
        rekebisha.quantity = quantity
        rekebisha.route = route

        rekebisha.save()
        return redirect('view_orders')
    else:
        d = OrderForm.objects.get(id=id)
        return render(request, 'edit.html', {'d': d})


def delete(request, id):
    d = OrderForm.objects.get(id=id)
    d.delete()
    return redirect('view_orders')
