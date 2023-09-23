from django.shortcuts import render,redirect
from .models import FoodItem, Donor
from .forms import FoodItemForm
from .forms import DonorForm


def food_item_list(request):
    food_items = FoodItem.objects.all()
    return render(request, 'wastage_collection/food_item_list.html', {'food_items': food_items})

def donor_list(request):
    donors = Donor.objects.all()
    return render(request, 'wastage_collection/donor_list.html', {'donors': donors})

def analytics(request):
    # Implement data analytics logic here
    # You can pass data to your analytics template
    return render(request, 'wastage_collection/analytics.html', {})

def create_food_item(request):
    if request.method == 'POST':
        form = FoodItemForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            form.save()
            # Redirect to a success page or another view
            return redirect('success_page')
    else:
        form = FoodItemForm()

    return render(request, 'wastage_collection/food_item_form.html', {'form': form})

def create_donor(request):
    if request.method == 'POST':
        form = DonorForm(request.POST)
        if form.is_valid():
            # Save the donor information to the database
            form.save()
            # Redirect to a success page or another view
            return redirect('success_page')
    else:
        form = DonorForm()

    return render(request, 'wastage_collection/donor_form.html', {'form': form})