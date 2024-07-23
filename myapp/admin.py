from django.contrib import admin
from .models import registration
from .models import category
from .models import product
from .models import order
from .models import feedback
from .models import contactus
from .models import cart

# Register your models here.
class showregistration(admin.ModelAdmin):
    list_display = ('r_name','r_password','r_mail','r_mobile','r_address')

class showrcategory(admin.ModelAdmin):
    list_display = ('id','category_name')

class showproduct(admin.ModelAdmin):
    list_display = ('p_name','p_price','p_cid','p_des','p_qua','p_status','admin_photo')
    list_per_page = 4
    list_filter = ['p_name','p_price']
    search_fields = ['p_name','p_cid__category_name']

class showcart(admin.ModelAdmin):
    list_display = ('product_id','customer_id','order_qua','order_totalprice','orderid','productstatus')

class showorder(admin.ModelAdmin):
    list_display = ('customer_id','totoalamount','timestamp')

class showfeedback(admin.ModelAdmin):
    list_display = ('login_id','rating','comment')

class showcontactus(admin.ModelAdmin):
    list_display = ('email','phone','message','timestamp')

admin.site.register(registration, showregistration)
admin.site.register(category, showrcategory)
admin.site.register(product, showproduct)
admin.site.register(order, showorder)
admin.site.register(feedback, showfeedback)
admin.site.register(contactus,showcontactus)
admin.site.register(cart,showcart)