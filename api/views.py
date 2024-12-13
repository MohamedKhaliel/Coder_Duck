from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Blog , Tag , Category , Comment , UserProfile
from .serializers import BlogSerializer , TagSerializer , CategorySerializer , CommentSerializer, UserProfileSerializer
from rest_framework.response import Response
from rest_framework import generics 
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet 
from rest_framework.permissions import IsAdminUser , IsAuthenticated , IsAuthenticatedOrReadOnly

# Create your views here.

class BlogList(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=201)

class UserProfileList(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes=[IsAuthenticated]

# class UserProfileView(APIView):
#     def get(self, request, *args, **kwargs):
#         user_profile = UserProfile.objects.get(user=request.user)
#         serializer = UserProfileSerializer(user_profile)
#         return Response(serializer.data)
    
class tagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAdminUser]

class CommentViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = CommentSerializer