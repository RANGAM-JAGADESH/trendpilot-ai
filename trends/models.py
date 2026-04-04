from django.db import models

class Trend(models.Model):
    title = models.CharField(max_length=300)
    source = models.CharField(max_length=100)
    url = models.URLField()
    summary = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title