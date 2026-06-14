from django.db import models

class Category(models.Model):
    name =models.CharField(max_length=100,  unique=True)
    #null=true diyerek dbnin boş bir değer kabul etmesini etkiliyoruz, blank dediğimizde formdan boş değer gelmeini.
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name
