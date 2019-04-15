from django.db import models

# Create your models here.


class dict_theme(models.Model):
    name = models.CharField(max_length=30)
    print(name)

    class Meta:
        db_table = "dict_theme"

