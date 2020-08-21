from django.urls import path, include
from .views import  article_list, article_details, ArticleAPIView, ArticleDetails, GenericAPIView, ArticleViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')

urlpatterns = [
    path('viewset/', include(router.urls)),
    #path('article/', article_list),
    path('article/', ArticleAPIView.as_view()),
    path('generics/article/<int:id>/', GenericAPIView.as_view()),
    #path('details/<int:pk>', ),
    path('details/<int:id>/', ArticleDetails.as_view()),
]