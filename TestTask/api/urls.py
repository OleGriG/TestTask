from django.urls import path

from .views import (
    get_weather, SendEmailAPIView, SortNumbersAPIView,
    ArticleListCreateView, ArticleRetrieveUpdateDestroyView
    )


app_name = 'api'


urlpatterns = [
    path('weather/', get_weather, name='weather'),
    path('sendmail/', SendEmailAPIView.as_view(), name='send_email'),
    path('sort/', SortNumbersAPIView.as_view(), name='sort'),
    path('articles/', ArticleListCreateView.as_view(),
         name='article-list-create'
         ),
    path('articles/<int:pk>/', ArticleRetrieveUpdateDestroyView.as_view(),
         name='article-retrieve-update-destroy'
         ),
]
