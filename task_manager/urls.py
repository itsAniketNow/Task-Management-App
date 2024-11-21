from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.contrib.auth.views import LogoutView # Import for the logout.
from tasks import views  # Import views from the tasks app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'), # For user login
    path('logout/', views.custom_logout_view, name='logout'), # For user logout
    path('', views.task_list, name='task_list'),  # Root URL points to task_list view
    path('tasks/', include('tasks.urls')),  # All other tasks URLs
    path('auth/', include('social_django.urls', namespace='social')),  # Google login
]
