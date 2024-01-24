from django.db import models

# Create your models here.
class  Toy (models.Model) :
    name =models.CharField(max_length=49)
    description= models.TextField(verbose_name="description", blank=True,null=True)
    price= models.DecimalField(max_digits=10, decimal_places=2, verbose_name="price")
    image = models.ImageField(upload_to='toy_images/', verbose_name="toy's image", blank=True, null=True)
    stock=models.PositiveIntegerField(default=0,verbose_name="stock")
    created_at =models.DateTimeField(auto_now_add=True,verbose_name="created at")
    updated_at=models.DateTimeField(auto_now=True , verbose_name="updated at")

    def __str__(self):
        return self.name
    
    class Meta:
         verbose_name="toy"
         verbose_name_plural="toys"
    

   