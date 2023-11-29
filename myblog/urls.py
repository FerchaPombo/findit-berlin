
from django.urls import path
from .views import PostList, PostDetail, like_post, add_comment


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', PostList.as_view(), name='post_list'),
    path('post<slug:slug>/', PostDetail.as.view(), name='post_detail'),
    path('like/<int:pk>/', like_post, name='like_post'),
    path('post/<slug:slug>/comment', add_comment, name='add_comment'),
]
