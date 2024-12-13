from django.urls import path , include
from . import views 
from .views import CommentViewSet 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('tags', views.tagViewSet),
# router.register('comments' , views.CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('blogs/', views.BlogList.as_view()),
    path('profiles/', views.UserProfileList.as_view()),
    ]