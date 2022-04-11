from django.urls import path

from .api_views import list_blogs, show_blog_detail


urlpatterns = [
    path("blogs/", list_blogs, name="list_blogs"),
    path("blogs/<int:pk>/", show_blog_detail, name="show_blog_detail")
]
