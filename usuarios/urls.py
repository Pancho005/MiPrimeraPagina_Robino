from django.contrib import admin
from django.urls import path, include
from usuarios.views import iniciar_sesion
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("iniciar-sesion/", iniciar_sesion, name="iniciar_sesion"),
    path('usuarios/', LogoutView.as_view(template_name='cerrar_sesion.html'), name="cerrar_sesion")
]

"""LogoutView.as_view(template_name='cerrar_sesion.html')
"""