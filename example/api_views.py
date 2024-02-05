from django.http import JsonResponse
import json
from .models import Blog, Comment


def list_blogs(request):
    # Get all of the blogs
    blogs = Blog.objects.all()

    # Turn the blogs into titles and urls
    response = []
    for blog in blogs:
        response.append({
            "title": blog.title,
            "content" : blog.content,
            "href" : blog.get_api_url(),
        })

    # Return the blogs in a JsonResponse
    return JsonResponse({"response, all blogs": response})


def show_blog_detail(request, id):
    # Get the blog
    blog = Blog.objects.get(id=id)

    # Return the blog and its comments in dictionary
    comments = [
        {"id": comment.id, "comment": comment.content} for comment in blog.comments.all() #blogs accesses Comment model thru the related_name=comments
    ]
    # comments = []  #version easier to understand than the one above^^
    # for comment in blog.comments.all():  #accesses comments trough the related_name: comments then it adds it to the list
    #     comment_data = {
    #         "id": comment.id,
    #         "comment": comment.content,   #this is the content attribute under the Comment model
    # }
    # comments.append(comment_data)

    response = {
        "title": blog.title,
        "content": blog.content,
        "href": blog.get_api_url(),
        "comments": comments,
    }

    # Return the JsonResponse
    return JsonResponse({"blog": response})


def create_comment(request, blog_id):
    if request.method == "POST":            #the white "body" on the right is for the information that the coder is going to input in insomnia
        body = json.loads(request.body)    #json.loads()  in Python that is used to parse a JSON string and convert it into a Python object(dic, array, int, etc)

        blog = Blog.objects.get(id=blog_id)
        # blog.add_comment(body["comment"]) # it passes body[comment] to models def add_comment function. ##uncomment to see how it works

        #uses Django's Oject-Relational Mapping(ORM) system to create a new intance of 'Comment' model and saves it in the database, creates a new comment
        Comment.objects.create(  #was moved to models  comment entire thing to see how blog.addcomment.etc works
            content=body["comment"], #using key:value, in this case accessing the python body dictionary. body = { "comment": "This is a comment"} and we use body["comment"] to get the value "This is a comment"
            blog=blog,  #associates the comment with the current blog
        )

        return JsonResponse({"message": "created"})  #lets the client(coder know that the comment that is inside body["comment"] has been created) in insomnia
