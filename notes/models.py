from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

class Title(models.Model):
    title_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title_text


class Body(models.Model):
    title = models.OneToOneField(Title, on_delete=models.CASCADE)
    body_text = models.TextField()

    def __str__(self):
        return self.body_text