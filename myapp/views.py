from django.db.models import Sum

from .models import registration , product , cart , order, feedback, category
from django.contrib import messages

# Create your views here.
from django.shortcuts import render, redirect


def indexpage(request):
    djgetdata = product.objects.filter(p_cid=category(id=13))
    context = {
        'data': djgetdata
    }
    return render(request,"index.html", context)

def checklogindata(request):
    if request.method == 'POST':
        usermail = request.POST.get("r_mail")
        userpass = request.POST.get("r_password")
        try:
            userdetails = registration.objects.get(r_mail=usermail, r_password = userpass)
            request.session["logid"] = userdetails.id
            request.session["logname"] = userdetails.r_name
            request.session.save()
        except:
            userdetails = None

        if userdetails is not None:
            messages.success(request,"Login Successfully!")
        else:
            messages.success(request, "incorrect details!")
    else:
        pass
    return render(request,"index.html")

def fetchdata(request):
    if request.method == 'POST':
        umail = request.POST.get("r_mail")
        try:
            userdetails = registration.objects.get(r_mail=umail)
        except:
            userdetails= None

        if userdetails is not None:
            messages.success(request,"You are Already registered")
            return render(request,"index.html")

        else:
            username = request.POST.get("r_name")
            useremail = request.POST.get("r_mail")
            userphone = request.POST.get("r_mobile")
            userpass = request.POST.get("r_password")
            useraddress = request.POST.get("r_address")

            insertdata = registration( r_name= username, r_mail= useremail, r_mobile = userphone, r_password = userpass, r_address= useraddress)
            insertdata.save()

            messages.success(request,"Registered Successfully!")
    else:
        pass
    return render(request,"index.html")

def checkoutpage(request):
    uid = request.session["logid"]
    getdata = cart.objects.filter(customer_id=uid,productstatus=0)
    carttotal = cart.objects.filter(customer_id=uid, productstatus=0).aggregate(Sum("order_totalprice"))
    carttotal = carttotal.get("order_totalprice__sum")
    print(carttotal)
    context = {
        'data':getdata,
        'total':carttotal
    }
    return render(request,"checkout.html",context)

def aboutpage(request):
    return render(request,"about.html")

def singlepage(request,id):
    getdata = product.objects.get(id=id)
    context = {
        'data':getdata
    }
    return render(request,"single.html",context)

def single2page(request):
    return render(request,"single2.html")

def contactpage(request):
    return render(request,"contact.html")

def productpage(request):
    getdata = product.objects.all()
    context = {
        'data':getdata
    }
    return render(request,"product.html",context)

def product2page(request):
    return render(request,"product2.html")

def faqspage(request):
    return render(request,"faqs.html")

def helppage(request):
    return render(request,"help.html")

def iconspage(request):
    return render(request,"icons.html")

def paymentpage(request):
    return render(request,"payment.html")

def privacypage(request):
    return render(request,"privacy.html")

def termspage(request):
    return render(request,"terms.html")

def typographypage(request):
    return render(request,"typography.html")

def categorywiseproduct(request,id):
    getdata = product.objects.filter(p_cid=id)
    context = {
        'data':getdata
    }
    return render(request,"categorywiseproduct.html",context)

def addtocart(request):
    uid = request.session["logid"]
    quantity = request.POST.get("quantity")
    pid = request.POST.get("pid")
    price = request.POST.get("price")
    print(pid)
    price = int(price)
    quantity = int(quantity)
    tprice = price * quantity
    insertquery = cart(product_id=product(id=pid),customer_id=registration(id=uid),order_qua=quantity,order_totalprice=tprice,orderid=0,productstatus=0)
    insertquery.save()
    messages.success(request,"Added to cart")
    return redirect(checkoutpage)

def deleteproduct(request,id):
    uid = request.session["logid"]
    queryremove = cart.objects.get(id=id,customer_id=uid)
    queryremove.delete()
    return redirect(checkoutpage)

def placeorder(request):
    uid = request.session["logid"]
    carttotal = cart.objects.filter(customer_id=uid, productstatus=0).aggregate(Sum("order_totalprice"))
    carttotal = carttotal.get("order_totalprice__sum")
    orderdata = order(customer_id=registration(id=uid),totoalamount=carttotal)
    orderdata.save()

    lasstid = order.objects.latest('id')

    print(lasstid)

    objid = lasstid.id
    print(objid)

    obj = cart.objects.filter(customer_id=registration(id=uid), productstatus=0)
    for object in obj:
        object.orderid = objid
        object.productstatus = 1
        object.save()
    messages.success(request,"order placed successfully")
    return redirect(feedbackpage)

def yourorders(request):
    uid = request.session["logid"]
    data = order.objects.filter(customer_id=uid)
    context = {
        'data':data
    }
    return  render(request,"yourorders.html",context)

def singleorder(request,id):
    data = cart.objects.filter(orderid=id)
    context = {
        'data':data
    }
    return render(request,"yourordersingle.html",context)

def feedbackpage(request):
    return render(request,"feedback.html")

def cartdetailspage(request):
    uid = request.session["logid"]
    getdata = cart.objects.filter(customer_id=uid, productstatus=0)
    carttotal = cart.objects.filter(customer_id=uid, productstatus=0).aggregate(Sum("order_totalprice"))
    carttotal = carttotal.get("order_totalprice__sum")
    print(carttotal)
    context = {
        'data': getdata,
        'total': carttotal
    }
    return render(request, "checkout.html", context)
   

def fetchfeedback(request):
    uid = request.session["logid"]
    if request.method=='POST':
        desc=request.POST.get("des")
        rat=request.POST.get("input-1")
        print(type(rat))
        print(rat)
        print(uid)
        feedbackdata=feedback(login_id=registration(id=uid),rating=rat,comment=desc)
        feedbackdata.save()
        messages.success(request,"Your Feedback is successfully Placed")
        return render(request, "index.html")

    else:
        pass
    return render(request,"index.html")


