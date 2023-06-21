"""onlineshopping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from siteadmin import views as adminview
from buyer import views as buyerview
from seller import views as sellerview
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',adminview.index,name="index"),
    path('login/',adminview.login,name="login"),
    path('loginAction/',adminview.loginAction,name="loginAction"),
    path('category/',adminview.category,name="category"),
    path('nameAction/',adminview.nameAction,name="nameAction"),
    path('buyerlogin/',buyerview.buyerlogin,name="buyerlogin"),
    path('buyerAction/',buyerview.buyerAction,name="buyerAction"),
    path('sellerlogin/',sellerview.sellerlogin,name="sellerlogin"),
    path('sellerAction/',sellerview.sellerAction,name="sellerAction"),
    path('viewseller/',adminview.viewseller,name="viewseller"),
    path('approve<int:id>/',adminview.approve,name="approve"),
    path('reject<int:id>/',adminview.reject,name="reject"),
    path('checkusername/',buyerview.checkusername,name="checkusername"),
    path('sellerhomepage/',sellerview.sellerhomepage,name="sellerhomepage"),
    path('addproducts/',sellerview.addproducts,name="addproducts"),
    path('productAction/',sellerview.productAction,name="productAction"),
    path('viewproducts/',sellerview.viewproducts,name="viewproducts"),
    path('delete<int:id>/',sellerview.delete,name="delete"),
    path('update<int:id>/',sellerview.update,name="update"),
    path('updateproducts/',sellerview.updateproducts,name="updateproducts"),
    path('buyersviewing/',buyerview.buyersviewing,name="buyersviewing"),
    path('buyerupdate/',buyerview.buyerupdate,name="buyerupdate"),
    path('buyerupdateAction/',buyerview.buyerupdateAction,name="buyerupdateAction"),
    path('updatesellerprofile/',sellerview.updatesellerprofile,name="updatesellerprofile"),
    path('sellerupdateAction/',sellerview.sellerupdateAction,name="sellerupdateAction"),
    path('addtocart<int:id>/',buyerview.addtocart,name="addtocart"),
    path('cartAction/',buyerview.cartAction,name="cartAction"),
    path('yourorders/',buyerview.yourorders,name="yourorders"),
    path('deletecart<int:id>/',buyerview.deletecart,name="deletecart"),
    path('orderAction/',buyerview.orderAction,name="orderAction"),
    path('orders/',buyerview.orders,name="orders"),
    path('orderdetails<int:id>/',buyerview.orderdetails,name="orderdetails"),
    path('cancelorder<int:id>/',buyerview.cancelorder,name="cancelorder"),
    path('viewbuyerorder/',sellerview.viewbuyerorder,name="viewbuyerorder"),
    path('moredetails<int:id>/',sellerview.moredetails,name="moredetails"),
    path('approveorder<int:id>/',sellerview.approveorder,name="approveorder"),
    path('rejectorder<int:id>/',sellerview.rejectorder,name="rejectorder"),
    path('tracking<int:id>/',sellerview.tracking,name="tracking"),
    path('trackingAction/',sellerview.trackingAction,name="trackingAction"),
    path('trackyourorder<int:id>/',buyerview.trackyourorder,name="trackyourorder"),
    path('forgotpass/',adminview.forgotpass,name="forgotpass"),
    path('forgotpassAction/',adminview.forgotpassAction,name="forgotpassAction"),
    path('checkpassAction/',adminview.checkpassAction,name="checkpassAction"),
    path('newpassAction/',adminview.newpassAction,name="newpassAction"),
    path('searchproduct/',buyerview.searchproduct,name="searchproduct"),
    path('searchAction/',buyerview.searchAction,name="searchAction"),
    path('searchcategory/',buyerview.searchcategory,name="searchcategory"),
    path('categorysearchAction/',buyerview.categorysearchAction,name="categorysearchAction"),
    path('logout/',adminview.logout,name="logout"),
    path('quickpasschange/',buyerview.quickpasschange,name="quickpasschange"),
    path('quickpasschangeAction/',buyerview.quickpasschangeAction,name="quickpasschangeAction"),
    path('paynow<int:id>/',buyerview.paynow,name="paynow"),
    path('payment/',buyerview.payment,name="payment"),
    path('deleteorderview<int:id>/',buyerview.deleteorderview,name="deleteorderview"),
    path('quickpasschangeseller/',sellerview.quickpasschangeseller,name="quickpasschangeseller"),
    path('sellerquickpasschangeAction/',sellerview.sellerquickpasschangeAction,name="sellerquickpasschangeAction"),
    path('adminpasschange/',adminview.adminpasschange,name="adminpasschange"),
    path('adminquickpasschangeAction/',adminview.adminquickpasschangeAction,name="adminquickpasschangeAction")
    
]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
