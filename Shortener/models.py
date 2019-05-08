from django.db import models


class ShortURL(models.Model):
   # Original link.
   original=models.URLField(max_length=300)
   # Short version of the link.
   short=models.CharField(max_length=50)
   def __str__ (self):
      return self.short+ " ==> " + self.original 

