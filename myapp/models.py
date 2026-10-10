from django.db import models

class User(models.Model):
    username =models.CharField(max_length=50)
    eamil = models.EmailField(max_length=254)
    
    
    def __str__(self):
        return self.username
    
    
class Category(models.Model):
    name =models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    cread_at = models.DateField(auto_now=False, auto_now_add=False)
    
    def __str__(self):
        return self.title
    
class rewiev(models.Model):
    text = models.TextField()
    rating = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
            return self.text