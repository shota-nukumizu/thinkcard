from django.db import models

class IdeaModel(models.Model):
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=70)
    content = models.TextField()
    post_data = models.DateField(auto_now=True)
    good = models.IntegerField(null=True, blank=True, default=0)
    interest = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return self.title