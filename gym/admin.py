from django.contrib import admin
from .models import MembershipPlan, MemberProfile, MembershipApplication

@admin.register(MembershipPlan)
class MembershipPlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'duration_months')

@admin.register(MemberProfile)
class MemberProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'membership_plan', 'is_active')

@admin.register(MembershipApplication)
class MembershipApplicationAdmin(admin.ModelAdmin):
    list_display = ('user', 'plan', 'status', 'applied_on')
    list_filter = ('status', 'plan')
