from django.db import models
from post.models import Post

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=None)
    content = models.TextField(default="Your Default Value Here")
    def __str__(self):
        return f"Comment to '{self.post.title}'"
    
    id = models.AutoField(primary_key=True)