from django.urls import reverse
from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def get_api_url(self):
        return reverse("show_blog_detail", kwargs={"pk": self.pk})


class Comment(models.Model):
    content = models.TextField()

    blog = models.ForeignKey(
        Blog,
        related_name="comments",
        on_delete=models.CASCADE,
    )
