from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponse
from django.shortcuts import redirect

# Пример представления для корневого URL
def home(request):
    return HttpResponse("Welcome to Foodgram!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/users/', include('users.urls')),
    path('', home, name='home'),  # или используйте перенаправление
    # path('', lambda request: redirect('api/', permanent=True)),
]
