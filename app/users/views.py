from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from .serializers import SignUpSerializer

User = get_user_model()

class SignUpView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer
    permission_classes = [AllowAny]
    authentication_classes = []