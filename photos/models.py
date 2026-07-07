from django.db import models

class Photographer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    profile_pic = models.ImageField(upload_to='profiles/')

    def __str__(self):
        return self.name


class Photo(models.Model):
    photographer = models.ForeignKey(Photographer,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos/')
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Booking(models.Model):
    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    event_date = models.DateField()
    message = models.TextField()

    def __str__(self):
        return self.customer_name