from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from dj_rest_auth.views import LoginView
from .airtable.comerciales import get_comercial_by_email

class UserDetailsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Como la solicitud ya está autenticada, podemos acceder a request.user.
        user = request.user

        # Ahora obtenemos la información del usuario desde Airtable.
        if user.user_type == 2:  # Si el usuario es un 'comercial'
            airtable_info = get_comercial_by_email(user.email)

            if airtable_info is not None:
                # Extraer la información relevante del comercial
                comercial_info = {
                    'nombre': airtable_info.get('Nombre'),
                    'telefono': airtable_info.get('Teléfono'),
                    'correo': airtable_info.get('Correo'),
                    'lider': airtable_info.get('Lider'),
                }
                return Response(comercial_info)

        # Si el usuario no es un 'comercial', solo devolvemos una respuesta vacía.
        return Response({})

class CustomLoginView(LoginView):
    def get_response(self):
        orginal_response = super().get_response()

        mydata = {"user_type": self.user.user_type}
        orginal_response.data.update(mydata)

        return orginal_response
