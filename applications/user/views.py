from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import User
from .serializers import UserCreateSerializer, UserUpdateSerializer, UserDefaultSerializer


# clase que me permita redireccionar al login django como primera vista
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.shortcuts import redirect

from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.shortcuts import redirect


class CustomLoginView(LoginView):
    def get(self, request, *args, **kwargs):
        # Si el usuario ya está autenticado, redirigir al panel de administración
        if request.user.is_authenticated:
            return redirect(reverse_lazy('admin:index'))
        return super().get(request, *args, **kwargs)

    # Si deseas usar una plantilla personalizada, la especificas aquí:
    def get_template_names(self):
        return ['admin/']  # Puedes cambiarla si tienes una plantilla personalizada




class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        elif self.action in ['update', 'partial_update']:
            return UserUpdateSerializer
        elif self.action in ['list', 'retrieve']:
            return UserDefaultSerializer
        return super().get_serializer_class()
