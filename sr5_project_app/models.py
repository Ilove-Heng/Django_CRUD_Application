from django.db import models
from django.utils import timezone


class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    published_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"""
            Title: {self.title} 
            Content: {self.content}
            Published at: {self.published_at.strftime('%Y-%m-%d %H:%M:%S')}
        """
class Meta : 
    db_table = 'article'