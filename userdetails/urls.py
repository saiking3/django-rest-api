from django.urls import path
from .views import article_list, article_details, ArticleAPIView, ArticleDetails

urlpatterns = [
    #path('article/', article_list),
    path('article/', ArticleAPIView.as_view()),
    #path('details/<int:pk>', ),
    path('details/<int:id>', ArticleDetails.as_view()),
]