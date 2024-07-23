from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.
class registration(models.Model):
    r_name = models.CharField(max_length=50)
    r_password = models.CharField(max_length=8)
    r_mail = models.EmailField(max_length=25)
    r_mobile = models.IntegerField()
    r_address = models.CharField(max_length=40)

    def __str__(self):
        return self.r_name

class category(models.Model):
    category_name = models.CharField(max_length=25)

    def __str__(self):
        return self.category_name

class product(models.Model):
    p_name = models.CharField(max_length=50)
    p_price = models.IntegerField()
    p_cid = models.ForeignKey(category,on_delete=models.CASCADE,null=True)
    p_des = models.TextField(max_length=500)
    p_qua = models.IntegerField()
    p_status = models.CharField(max_length=30)
    p_image = models.ImageField(upload_to='photos')

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.p_image.url))

    admin_photo.allow_tags = True

    def __str__(self):
        return self.p_name

class cart(models.Model):
    product_id = models.ForeignKey(product,on_delete=models.CASCADE,null=True)
    customer_id = models.ForeignKey(registration,on_delete=models.CASCADE,null=True)
    order_qua = models.IntegerField()
    order_totalprice = models.IntegerField()
    orderid = models.IntegerField()
    productstatus = models.IntegerField()

class order(models.Model):
    customer_id = models.ForeignKey(registration, on_delete=models.CASCADE, null=True)
    totoalamount = models.IntegerField()
    timestamp = models.DateTimeField(auto_now=True)

class feedback(models.Model):
    login_id = models.ForeignKey(registration,on_delete=models.CASCADE,null=True)
    rating = models.IntegerField(max_length=10)
    comment = models.CharField(max_length=100)

class contactus(models.Model):
    email = models.EmailField(max_length=25)
    phone = models.IntegerField()
    message = models.TextField()
    timestamp = models.DateTimeField(max_length=30)



