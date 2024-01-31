from rest_framework import serializers
from ..models import UsuarioModel

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioModel
        fields = '__all__'