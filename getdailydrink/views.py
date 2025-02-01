from django.shortcuts import render, redirect
from .forms import WaterIntakeForm
from .models import UserWaterIntake
from users.models import CustomerUser
from datetime import datetime
from django.db.models import Sum

# Create your views here.


def calculate_water_intake(gender, exercises_type, location):
    water_amount = 2.5

    if gender == 'male':
        water_amount += 0.13
    
    if exercises_type == 'cardio':
        water_amount += 0.5
    
    elif exercises_type == 'weights':
        water_amount += 0.3

    if location.lower() == 'tropical':
        water_amount += 1.7

    return water_amount


def dashboard(request):
    intake = UserWaterIntake.objects.filter(user=request.user).order_by('-timestamp')
    user= request.user
    profile = CustomerUser.objects.get(id=user.id)
    recommanded_intake = calculate_water_intake(profile.gender, profile.exercises_type, profile.location)

    total_today = intake.filter(timestamp__date=datetime.today().date()).aggregate(total=Sum('water_amount'))['total'] or 0
    remaining_intake = max(recommanded_intake - total_today, 0)

    context = {
        'intake' : intake,
        'remaining_intake' : remaining_intake,
        'total_today' : total_today,
        'recommanded_intake' : recommanded_intake,
    }

    return render(request, 'pages/index.html', context)


def log_water(request):
    if request.method == 'POST':
        form = WaterIntakeForm(request.POST)
        if form.is_valid():
            gender = request.POST['gender']
            exercises_type = request.POST['exercises_type']
            location = request.POST['location']

            water_amount = calculate_water_intake(gender, exercises_type, location)

            user_entry = UserWaterIntake.objects.create(
                user=request.user,
                exercises_type=exercises_type,
                water_amount=water_amount,
            )
            user_entry.save()
            return redirect('dashboard')
    else:
        form = WaterIntakeForm()

    return render(request, 'pages/log_water.html', {'form': form})

