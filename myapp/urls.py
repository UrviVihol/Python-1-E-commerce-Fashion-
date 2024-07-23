
from django.urls import path
from . import views

urlpatterns = [
    path('',views.indexpage,name="index.html"),
    path('checkout',views.checkoutpage,name="checkout.html"),
    path('contact', views.contactpage, name="contact.html"),
    path('single', views.singlepage, name="single.html"),
    path('singlepage/<int:id>', views.singlepage, name="single.html"),
    path('single2', views.single2page, name="single2.html"),
    path('about', views.aboutpage, name="about.html"),
    path('product', views.productpage, name="product.html"),
    path('product2', views.product2page, name="product2.html"),
    path('icons', views.iconspage, name="icons.html"),
    path('help', views.helppage, name="help.html"),
    path('payment', views.paymentpage, name="payment.html"),
    path('privacy', views.privacypage, name="privacy.html"),
    path('terms', views.termspage, name="terms.html"),
    path('typography', views.typographypage, name="typography.html"),
    path('faqs', views.faqspage, name="faqs.html"),
    path('checklogindata',views.checklogindata,name="checklogindata"),
    path('fetchdata',views.fetchdata,name="fetchdata"),
    path('addtocart',views.addtocart,name="addtocart"),
    path('placeorder',views.placeorder,name="placeorder"),
    path('yourorder',views.yourorders,name="yourorder"),
    path('feedback',views.feedbackpage,name="feedback"),
    path('cartdetails',views.cartdetailspage,name="cartdetails"),
    path('fetchfeedback',views.fetchfeedback,name="fetchfeedback"),

    path('delete/<int:id>',views.deleteproduct, name="deleteproduct"),
    path('singleorder/<int:id>',views.singleorder, name="singleorder"),
    path('categorywiseproduct/<int:id>',views.categorywiseproduct,name="categorywiseproduct"),
]
