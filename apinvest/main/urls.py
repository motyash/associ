from django.urls import path, include
from . import views
from django.contrib import admin
import nested_admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('nested_admin/', include('nested_admin.urls')),
    path('', views.home, name='home'),
    path('<slug:slug>/', views.home, name='tab'),
]
