from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_cad_usuarios.urls')),  # Inclui as rotas da app
]
