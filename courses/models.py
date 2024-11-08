from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    image = models.ImageField(upload_to='course_images/', blank=True, null=True)  # Image field

    def discounted_price(self):
        return self.price * (1 - self.discount / 100)

    def __str__(self):
        return self.name
