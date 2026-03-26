from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from gym import views as gym_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gym.urls')),
    path('shop/', include('shop.urls')),
    path('register/', gym_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='gym/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
