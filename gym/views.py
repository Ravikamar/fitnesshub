from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import MembershipPlan, MembershipApplication, MemberProfile
from .forms import UserRegisterForm, MembershipApplyForm

def home(request):
    plans = MembershipPlan.objects.all()[:3]
    return render(request, 'gym/home.html', {'plans': plans})

def membership_plans(request):
    plans = MembershipPlan.objects.all()
    return render(request, 'gym/membership_plans.html', {'plans': plans})

@login_required
def apply_membership(request, plan_id):
    plan = get_object_or_404(MembershipPlan, id=plan_id)
    if request.method == 'POST':
        form = MembershipApplyForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.plan = plan
            application.save()
            messages.success(request, f'Your application for {plan.name} has been submitted!')
            return redirect('profile')
    else:
        form = MembershipApplyForm()
    return render(request, 'gym/apply_membership.html', {'form': form, 'plan': plan})

@login_required
def profile(request):
    applications = MembershipApplication.objects.filter(user=request.user)
    return render(request, 'gym/profile.html', {'applications': applications})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'gym/register.html', {'form': form})
