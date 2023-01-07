from django.urls import path
from NewsPortal.views import ListNews, NewsDetail, SearchListView, NewsCreate, NewsUpdate, NewsDelete

urlpatterns = [
    path('news/', ListNews.as_view(), name='news'),
    path('search/', SearchListView.as_view(), name='news_search'),
    path('news/<pk>', NewsDetail.as_view(), name='news_detail'),
    path('news/create/', NewsCreate.as_view(), name='news_create'),
    path('post/create/', NewsCreate.as_view(), name='news_create'),
    path('news/<int:pk>/update/', NewsUpdate.as_view(), name='news_update'),
    path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('post/<int:pk>/update/', NewsUpdate.as_view(), name='news_update'),
    path('post/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
]