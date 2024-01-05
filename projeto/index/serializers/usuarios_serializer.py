from rest_framework import serializers
from models.usuario_model import Usuario

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'