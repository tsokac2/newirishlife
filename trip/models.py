from django.db import models


class Trip(models.Model):
    """
    Trip Section Model for trip template
    """
    main_title = models.CharField(max_length=254)
    sub_title_1 = models.CharField(max_length=254)
    sub_title_2 = models.CharField(max_length=254)
    sub_title_3 = models.CharField(max_length=254)

    def __str__(self):
        return self.main_title