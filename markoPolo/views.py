# valuables/views.py
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, filters, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Valuable
from .serializers import ValuableSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ValuableUploadView(APIView):
    """
    API endpoint for uploading a new Valuable object.
    """

    def post(self, request, format=None):
        serializer = ValuableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)  # Set the owner to the authenticated user
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ValuableList(generics.ListCreateAPIView):
    """
           List all snippets, or create a new snippet
    """
    queryset = Valuable.objects.all()
    serializer_class = ValuableSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'category', 'description', 'location', 'owner']
    search_fields = ['title', 'description', 'category', 'location']
    ordering_fields = ['title', 'category']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ValuableDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Valuable.objects.all()
    serializer_class = ValuableSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
