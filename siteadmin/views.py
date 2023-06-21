from django.shortcuts import render,redirect
from siteadmin.models import*
from buyer.models import*
from seller.models import*
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,"index.html")
def login(request):
    return render(request,"adminlogin.html")
def loginAction(request):
    username=request.POST['username']
    password=request.POST['password']
    admin=admin_tb.objects.filter(username=username,password=password)
    buyer=buyer_tb.objects.filter(username=username,password=password)
    seller=seller_tb.objects.filter(username=username,password=password)
    if admin.count()>0:
        request.session['id']=admin[0].id
        messages.add_message(request,messages.INFO,"Login successfull.")
        return render(request,"adminloginpage.html")
    elif buyer.count()>0:
        request.session['id']=buyer[0].id
        return render(request,"buyerhomepage.html")
    elif seller.count()>0:
        status=seller[0].status
        if status == "Approved":
            request.session['id']=seller[0].id
            return render(request,"sellerhomepage.html")
        else:
            return redirect('login')    
    else:
        return redirect('login')
def category(request):
    return render(request,"category.html")
def nameAction(request):
    name=request.POST['name']
    user=category_tb(name=name)
    user.save()
    messages.add_message(request,messages.INFO,"Category added succesfully.")
    return render(request,"category.html")
def viewseller(request):
    view=seller_tb.objects.all()
    return render(request,"viewseller.html",{'data':view})
def approve(request,id):
    a=seller_tb.objects.filter(id=id).update(status="Approved")
    return redirect('viewseller')
def reject(request,id):
    r=seller_tb.objects.filter(id=id).update(status="Rejected")
    return redirect('viewseller')
def forgotpass(request):
    return render(request,"forgotpass.html")
def forgotpassAction(request):
    username=request.POST['username']
    buyer=buyer_tb.objects.filter(username=username)
    seller=seller_tb.objects.filter(username=username)
    if buyer.count()>0:
        request.session['id']=buyer[0].id
        return render(request,"passchange.html",{'data':username})
    elif seller.count()>0:
        return render(request,"passchange.html",{'data':username})
    else:
        return redirect('forgotpass')
def checkpassAction(request):
    name=request.POST['name']
    phonenumber=request.POST['phonenumber']
    dob=request.POST['dob']
    country=request.POST['country']
    username=request.POST['username']
    buyer=buyer_tb.objects.filter(name=name,phonenumber=phonenumber,dob=dob,country=country)
    seller=seller_tb.objects.filter(name=name,phonenumber=phonenumber,dob=dob,country=country)
    if buyer.count()>0:
        return render(request,"changepassword.html",{'data':username})
    elif seller.count()>0:
        return render(request,"changepassword.html",{'data':username})
    else:
        return redirect('checkpassAction')
def newpassAction(request):
    password=request.POST['password']
    cnfpassword=request.POST['cnfpassword']
    username=request.POST['username']
    if password == cnfpassword:
        buyertb=buyer_tb.objects.filter(username=username)
        seller=seller_tb.objects.filter(username=username)
        if buyertb.count()>0:
            request.session['id']=buyertb[0].id
            buyerid=request.session['id']
            bpc=buyer_tb.objects.filter(id=buyerid).update(password=password)
            return redirect('index')
        elif seller.count()>0:
            request.session['id']=seller[0].id
            sellerid=request.session['id']
            spc=seller_tb.objects.filter(id=sellerid).update(password=password)
            return redirect('index')
        else:
            return redirect('login')
    else:
        return render(request,'changepassword.html',{'data':username})  
def logout(request):
    logout=request.session.flush()
    return redirect('login')      
def adminpasschange(request):
    adminid=request.session['id']
    apc=admin_tb.objects.filter(id=adminid)
    return render(request,"adminquickpasschange.html")
def adminquickpasschangeAction(request):
    adminid=request.session['id']
    opass=request.POST['adoldpass']
    npass=request.POST['adnewpass']
    cpass=request.POST['adcnfpass']
    admintb=admin_tb.objects.filter(id=adminid,password=opass)
    if admintb.count()>0:
            if npass == cpass:
                change=admin_tb.objects.filter(id=adminid).update(password=npass)
                messages.add_message(request,messages.INFO,"Password Updated Successfully")
            else:
                messages.add_message(request,messages.INFO,"Password Not Equal")
                return redirect('adminpasschange')

    else:
        messages.add_message(request,messages.INFO," Current Password Does not Match")
        return redirect('adminpasschange')


