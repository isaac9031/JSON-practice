from django.urls import reverse
from django.db import models


class Blog(models.Model):  #aggregate root
    title = models.CharField(max_length=200)
    content = models.TextField()

    # #uncomment to see how it works
    # def add_comment(self, content):  #part of it came from views, added here since it adds it to the comments list
    #     Comment.objects.create(  #comment = Comment.objects.create( not needed since we are accessing it thru blog in the api_view
    #         blog = self,  #self is used to associate the newly created Comment with the specific Blog instance
    #         content = content
    #     )
    #     # self.comments.add(comment) not needed since we access the Comment through blogs by using the realated name: comments

    def get_api_url(self):                                           # kwargs parameter is used to pass keyword arguments to the URL pattern.
        return reverse("show_blog_detail", kwargs={"id": self.id})   #In this case, you are passing a keyword argument "id" with the value self.id. self.id represents the primary key of the current instance of the Blog model.


class Comment(models.Model):  #aggregate
    content = models.TextField()

    blog = models.ForeignKey(
        Blog,
        related_name="comments",
        on_delete=models.CASCADE,
    )



# In summary, the Blog model is the aggregate root because it
# is the primary entity that manages the lifecycle of associated
# Comment entities. The Comment model is part of the aggregate,
# and it is associated with a specific Blog instance through a foreign key relationship.

# self refers to the instance of the Blog class that is calling the add_comment method.
# When you call blog_instance.add_comment(content), self will represent blog_instance.
# In this context, self is used to associate the newly created Comment with the specific
# Blog instance (blog_instance) by setting the blog foreign key field of the Comment model to
# self (the current Blog instance).


# In the get_api_url method:

# self is used to refer to the current instance of the Blog class. When you call
#  blog_instance.get_api_url(), self represents blog_instance.
# It is used to access the id attribute of the Blog instance, which is then used
# as a parameter in the reverse function to generate the URL for the show_blog_detail view.
