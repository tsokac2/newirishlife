from django.db import models


class Home(models.Model):
    """
    Home Section Model for home template
    """
    title = models.CharField(max_length=254)
    movie_quote = models.TextField(max_length=254)
    p_1 = models.TextField(max_length=254)
    p_2 = models.TextField(max_length=254)
    p_3 = models.TextField(max_length=254)

    def __str__(self):
        return self.title