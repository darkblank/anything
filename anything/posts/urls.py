from django.urls import path

from posts.views import PostList, PostDetail

app_name = 'posts'

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('<int:pk>/', PostDetail.as_view(), name='post_detail'),
]