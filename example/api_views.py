from django.http import JsonResponse

from .models import Blog


def list_blogs(request):
    # Get all of the blogs
    blogs = Blog.objects.all()

    # Turn the blogs into titles and urls
    response = []
    for blog in blogs:
        response.append({
            "title": blog.title,
            "href": blog.get_api_url()
        })

    # Return the blogs in a JsonResponse
    return JsonResponse({"blogs": response})


def show_blog_detail(request, pk):
    # Get the blog
    blog = Blog.objects.get(pk=pk)

    # Return the blog and its comments in dictionary
    comments = []
    for comment in blog.comments.all():
        comments.append({
            "content": comment.content
        })

    # Return the JsonResponse
    response = {
        "title": blog.title,
        "content": blog.content,
        "comments": comments
    }

    return JsonResponse(response)