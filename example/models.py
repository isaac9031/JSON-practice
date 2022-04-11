from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()


class Comment(models.Model):
    content = models.TextField()

    blog = models.ForeignKey(
        Blog,
        related_name="comments",
        on_delete=models.CASCADE,
    )
