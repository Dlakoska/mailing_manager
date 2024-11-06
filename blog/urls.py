from blog.apps import BlogConfig

from django.urls import path

from blog.views import BlogListView, BlogDetailView, BlogCreatView, BlogUpdateView, BlogDeleteView

# from blog.views import

app_name = BlogConfig.name


urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('create/', BlogCreatView.as_view(), name='blog_create'),
    path('<int:pk>/update', BlogUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', BlogDeleteView.as_view(), name='delete')
]
