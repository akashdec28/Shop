from django.shortcuts import render,redirect
from siteadmin.models import*
from buyer.models import*
from seller.models import*
from django.contrib import messages
import datetime

# Create your views here.
def sellerlogin(request):
    return render(request,"sellerregistration.html")
def sellerAction(request):
    name=request.POST['name']
    gender=request.POST['gender']
    dob=request.POST['dob']
    country=request.POST['country']
    phonenumber=request.POST['phonenumber']
    address=request.POST['address']
    username=request.POST['username']
    password=request.POST['password']    
    if len(request.FILES)>0:
        img=request.FILES['file']
    else:
        img="No Pic"
   
    user=seller_tb(name=name,gender=gender,dob=dob,country=country,phonenumber=phonenumber,address=address,username=username,password=password,file=img)
    user.save()
    messages.add_message(request,messages.INFO,"Registration Successfull")
    return render(request,"sellerregistration.html")
def sellerhomepage(request):
    return render(request,"sellerhomepage.html")
def addproducts(request):
    categoryid=category_tb.objects.all()
    return render(request,"addproducts.html",{'categoryid':categoryid})
def productAction(request):
    productname=request.POST['productname']
    if len(request.FILES)>0:
        img=request.FILES['productimage']
    else:
        img="No Pic"
    productprice=request.POST['productprice']
    productdetails=request.POST['productdetails']
    productstock=request.POST['productstock']
    categoryid=request.POST['category']
    sellerid=request.session["id"]
    product=product_tb(productname=productname,productimage=img,sellerid_id=sellerid,productprice=productprice,productdetails=productdetails,productstock=productstock,categoryid_id=categoryid)
    product.save()
    messages.add_message(request,messages.INFO,"Product uploaded successfully")
    return redirect('addproducts')
def viewproducts(request):
    sellerid=request.session['id']
    product=product_tb.objects.filter(sellerid_id=sellerid)
    return render(request,"viewproducts.html",{'data':product})
def delete(request,id):
    dp=product_tb.objects.filter(id=id).delete()
    return redirect('viewproducts')
def update(request,id):
    up=product_tb.objects.filter(id=id)
    return render(request,"updateproducts.html",{'update':up})
    messages.add_message(request,messages.INFO,"Product updation successfull")
def updateproducts(request):
    id=request.POST['id']
    sellerid=request.session['id']
    productname=request.POST['productname']
    productid=product_tb.objects.filter(id=id)
    if len(request.FILES)>0:
        img=request.FILES['productimage']
    else:
        productid[0].productimage
       
       
    productprice=request.POST['productprice']
    productdetails=request.POST['productdetails']
    productstock=request.POST['productstock']
    
    product=product_tb.objects.filter(id=id).update(productname=productname,productprice=productprice,productdetails=productdetails,productstock=productstock,productimage=img)
    product_object=product_tb.objects.get(id=id)
    product_object.productimage=img
    product_object.save()
    return redirect('viewproducts')
def updatesellerprofile(request):
    su=request.session['id']
    sel=seller_tb.objects.filter(id=su)
    return render(request,"sellerprofileupdate.html",{'edit':sel})
def sellerupdateAction(request):
    id=request.POST['id']
    name=request.POST['name']
    gender=request.POST['gender']
    dob=request.POST['dob']
    country=request.POST['country']
    phonenumber=request.POST['phonenumber']
    address=request.POST['address']
    username=request.POST['username']
    password=request.POST['password']
    productid=seller_tb.objects.filter(id=id)
    if len(request.FILES)>0:
        img=request.FILES['file']
    else:
        img=productid[0].file
    su=seller_tb.objects.filter(id=id).update(name=name,gender=gender,dob=dob,country=country,phonenumber=phonenumber,address=address,username=username,password=password,file=img)
    product_object=seller_tb.objects.get(id=id)
    product_object.file=img
    product_object.save()
    return redirect('login')
def viewbuyerorder(request):
    sellproduct=product_tb.objects.filter(sellerid_id=request.session['id']).values('id')
    orderitems=orderitems_tb.objects.filter(productid_id__in=sellproduct).select_related('orderid').values('orderid_id')
    orders=order_tb.objects.filter(id__in=orderitems)
    return render(request,"viewbuyerorder.html",{'order':orders})
def moredetails(request,id):
    sellproduct=product_tb.objects.filter(sellerid_id=request.session['id']).values('id')
    orderitem=orderitems_tb.objects.filter(orderid=id,productid_id__in=sellproduct).select_related('orderid')
    order=order_tb.objects.filter(id=id)
    return render(request,"moredetails.html",{'details':order,'data':orderitem})
def approveorder(request,id):
    ao=order_tb.objects.filter(id=id).update(status="Approved")
    return redirect('viewbuyerorder')
def rejectorder(request,id):
    ro=order_tb.objects.filter(id=id).update(status="Rejected")
    return redirect('viewbuyerorder')
def tracking(request,id):
    to=order_tb.objects.filter(id=id)
    return render(request,"tracking.html",{'tracking':to})
def trackingAction(request):
    orderid=request.POST['id']
    order=order_tb.objects.get(id=orderid)
    date=datetime.date.today()
    time=datetime.datetime.now().strftime("%H:%M")
    discription=request.POST['discription']
    track=tracking_tb(orderid=order,date=date,time=time,discription=discription)
    track.save()
    return redirect('viewbuyerorder')
def quickpasschangeseller(request):
    sellerid=request.session['id']
    qpcs=seller_tb.objects.filter(id=sellerid)
    return render(request,"sellerquickpasschange.html")
def sellerquickpasschangeAction(request):
    sellerid=request.session['id']
    opass=request.POST['seloldpass']
    npass=request.POST['selnewpass']
    cpass=request.POST['selcnfpass']
    sellertb=seller_tb.objects.filter(id=sellerid,password=opass)
    if sellertb.count()>0:
            if npass == cpass:
                change=seller_tb.objects.filter(id=sellerid).update(password=npass)
                messages.add_message(request,messages.INFO,"Password Updated Successfully")
                return redirect('quickpasschangeseller')
            else:
                messages.add_message(request,messages.INFO,"Password Not Equal")
                return redirect('quickpasschangeseller')

    else:
        messages.add_message(request,messages.INFO," Current Password Does not Match")
        return redirect('quickpasschangeseller')


    
    
