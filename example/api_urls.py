from django.urls import path

from .api_views import list_blogs, show_blog_detail, create_comment


urlpatterns = [
    path("blogs/", list_blogs, name="list_blogs"),
    path("blogs/<int:id>/", show_blog_detail, name="show_blog_detail"),
    # path("blogs")
    path(
        "blogs/<int:blog_id>/comments/",
        create_comment,
        name="create_comment"
    )
]
