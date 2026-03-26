from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('memberships/', views.membership_plans, name='membership_plans'),
    path('apply/<int:plan_id>/', views.apply_membership, name='apply_membership'),
    path('profile/', views.profile, name='profile'),
]
