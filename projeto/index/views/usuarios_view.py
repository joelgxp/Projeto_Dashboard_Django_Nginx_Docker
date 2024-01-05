from rest_framework.views import APIView
from rest_framework.response import Response
from models.usuario_model import Usuario
from serializers.usuarios_serializer import UsuariosSerializer
from rest_framework import status as status_code

class UsuariosView(APIView):
    def get(self, request, format=None):
        usuarios = Usuario.objects.filter(tipo_usuario='L')
        serializer_usuarios = UsuariosSerializer(usuarios, many=True)
        return Response(serializer_usuarios.data, status=status_code.HTTP_200_OK)
    