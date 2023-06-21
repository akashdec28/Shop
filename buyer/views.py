from django.shortcuts import render,redirect
from siteadmin.models import*
from buyer.models import*
from seller.models import*
from django.contrib import messages
from django.http import JsonResponse
import datetime

# Create your views here.
def buyerlogin(request):
    return render(request,"buyerregistration.html")
def buyerAction(request):
    name=request.POST['name']
    gender=request.POST['gender']
    dob=request.POST['dob']
    country=request.POST['country']
    phonenumber=request.POST['phonenumber']
    address=request.POST['address']
    username=request.POST['username']
    password=request.POST['password']
    user=buyer_tb(name=name,gender=gender,dob=dob,country=country,phonenumber=phonenumber,address=address,username=username,password=password)
    user.save()
    messages.add_message(request,messages.INFO,"Registration Successfull")
    return render(request,"buyerregistration.html")
def checkusername(request):
    username=request.GET['username']
    user=buyer_tb.objects.filter(username=username)
    if len(user)>0:
        msg="exist"
    else:
        msg="notexist"
    return JsonResponse({'valid':msg})

def buyerupdate(request):
    bu=request.session['id']
    buy=buyer_tb.objects.filter(id=bu)
    return render(request,"buyerprofileupdate.html",{'edit':buy})
def buyerupdateAction(request):
    id=request.POST['id']
    name=request.POST['name']
    gender=request.POST['gender']
    dob=request.POST['dob']
    country=request.POST['country']
    phonenumber=request.POST['phonenumber']
    address=request.POST['address']
    username=request.POST['username']
    password=request.POST['password']
    bu=buyer_tb.objects.filter(id=id).update(name=name,gender=gender,dob=dob,country=country,phonenumber=phonenumber,address=address,username=username,password=password)
    messages.add_message(request,messages.INFO,"Profile updated Successfully")
    return redirect('login')

def buyersviewing(request):
    buyerid=request.session['id']
    view=product_tb.objects.all()
    return render(request,"buyerproductview.html",{'data':view})
def addtocart(request,id):
    p=product_tb.objects.filter(id=id)
    return render(request,"cart.html",{'data':p})
def cartAction(request):
    productid=request.POST['id']
    buyerid=request.session['id']
    phonenumber=request.POST['phonenumber']
    quantity=request.POST['quantity']
    shippingaddress=request.POST['shippingaddress']
    totalprice=request.POST['totalprice']
    stock=request.POST['stock']
    if  int(quantity) < int(stock):
        cart=cart_tb(productid_id=productid,buyerid_id=buyerid,phonenumber=phonenumber,quantity=quantity,shippingaddress=shippingaddress,totalprice=totalprice)
        cart.save()
    else:
        messages.add_message(request,messages.INFO,"Quantity is greater than stock")
    return redirect('buyersviewing')
def yourorders(request):
    buyerid=request.session['id']
    view=cart_tb.objects.filter(buyerid_id=buyerid)
    return render(request,"viewcart.html",{'data':view})
def deletecart(request,id):
    dc=cart_tb.objects.filter(id=id).delete()
    return redirect('yourorders')
def orderAction(request):
    buyerid=request.session['id']
    shippingaddress=request.POST['shippingaddress']
    phonenumber=request.POST['phonenumber']
    date=datetime.date.today()
    time=datetime.datetime.now().strftime("%H:%M")
    cartitems=request.POST.getlist("checkbox")
    if len(cartitems)!=0:
        orde=order_tb(buyerid_id=buyerid,shippingaddress=shippingaddress,phonenumber=phonenumber,date=date,time=time)
        orde.save()
        for cid in cartitems:
            cartitem=cart_tb.objects.filter(id=cid)
            totalprice=cartitem[0].totalprice
            quantity=cartitem[0].quantity
            buyerid=request.session['id']
            productid=cartitem[0].productid_id
            stock=cartitem[0].productid.productstock
            newstock=int(stock)-quantity
            product=product_tb.objects.filter(id=productid).update(productstock=newstock)
            cartitem.delete()
            o=orderitems_tb(totalprice=totalprice,quantity=quantity,buyerid_id=buyerid,productid_id=productid,orderid_id=orde.id)
            o.save()        
        return redirect('paynow',orde.id)           
    else:
        messages.add_message(request,messages.INFO,"Select atleast one item")
    return redirect('orders')
def orders(request):
    buyerid=request.session['id']
    view1=order_tb.objects.filter(buyerid_id=buyerid)
    return render(request,"orderview.html",{'data':view1})
def orderdetails(request,id):
    view1=order_tb.objects.filter(id=id)
    oi=orderitems_tb.objects.filter(orderid_id=id)
    return render(request,"orderdetails.html",{'data':view1,'od':oi})
def cancelorder(request,id):
    co=order_tb.objects.filter(id=id).update(status="cancelled")
    return redirect('orders')
def trackyourorder(request,id):
    vt=tracking_tb.objects.filter(orderid=id)
    return render(request,"trackingview.html",{'track':vt})
def searchproduct(request):
    return render(request,"searchproduct.html")
def searchAction(request):
    buyerid=request.session['id']
    search=request.POST['search']
    sp=product_tb.objects.filter(productname__istartswith=search)
    return render(request,"buyerproductview.html",{'data':sp})
def searchcategory(request):
    sc=category_tb.objects.all()
    return render(request,"viewcategory.html",{'categories':sc})
def categorysearchAction(request):
    ccategory=request.POST['category']
    cprice=request.POST['pricerange']
    pprice=product_tb.objects.filter(productprice__lte=cprice,categoryid_id=ccategory)
    return render(request,"buyerproductview.html",{'data':pprice})
def quickpasschange(request):
    buyerid=request.session['id']
    qpc=buyer_tb.objects.filter(id=buyerid)
    return render(request,"quickpasschange.html")
def quickpasschangeAction(request):
    buyerid=request.session['id']
    opass=request.POST['oldpass']
    npass=request.POST['newpass']
    cpass=request.POST['cnfpass']
    buyertb=buyer_tb.objects.filter(id=buyerid,password=opass)
    if buyertb.count()>0:
            if npass == cpass:
                change=buyer_tb.objects.filter(id=buyerid).update(password=npass)
                messages.add_message(request,messages.INFO,"Password Updated Successfully")
            else:
                messages.add_message(request,messages.INFO,"Password Not Equal")
                return redirect('quickpasschange')

    else:
        messages.add_message(request,messages.INFO," Current Password Does not Match")
        return redirect('quickpasschange')
def paynow(request,id):
    pay=orderitems_tb.objects.filter(orderid_id=id)
    return render(request,"payment.html",{'data':pay})
def payment(request):
    buyerid=request.session['id']
    orderid=request.POST['ordid']
    cardnumber=request.POST['cardnumber']
    cardname=request.POST['cardname']
    cvd=request.POST['cvd']
    expirydate=request.POST['expirydate']
    pa=payments_tb(buyerid_id=buyerid,orderid_id=orderid,cardnumber=cardnumber,cardname=cardname,cvd=cvd,expirydate=expirydate)
    pa.save()
    messages.add_message(request,messages.INFO,"Payment successfull")
    return redirect('orders')
def deleteorderview(request,id):
    delorder=order_tb.objects.filter(id=id).delete()
    return redirect('orders')


    
       
        
        
        