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

class CommentModel(models.Model):
    text = models.TextField()
    post = models.ForeignKey(IdeaModel, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:10]