from django.shortcuts import render
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import tbl_user1,tbl_products

from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import authentication_classes
from rest_framework import *
from django.contrib.auth import authenticate
import json

# Create your views here.
def success_response(response, status_code=None):
        json_obj = {
        "hasError": False,
        "errorCode": -1,
        "message": "Success",
        }
        json_obj["response"] = response
        if status_code is None:
            return Response(json_obj, status=status.HTTP_200_OK)
        return Response(json_obj, status=status_code)

def failure_response(response, status_code=None, error_code=1001, message="Failure"):
    json_obj = {
        "hasError": True,
        "errorCode": error_code,
        "message": message,
    }
    json_obj["response"] = response
    if status_code is None:
        return Response(json_obj, status=status.HTTP_200_OK)
    return Response(json_obj, status_code)

class createaccount(APIView):
     def post(self,request):
          datas={}
          response={}

          try:
               x = tbl_user1()
               y= User()
               x.username = request.data['user']
               x.first_name = request.data['fname']
               x.gender = request.data['gender']
               x.phone = request.data['ph']
               x.email = request.data['mail']
               x.place = request.data['place']
               photo = request.FILES['photo']
               fs=FileSystemStorage()
               filename=fs.save(photo.name,photo)
               uploaded_file_url=fs.url(filename)
               x.photo=uploaded_file_url
               x.address = request.data['adrs']

               y.username = request.data['user']
               password = request.data['pwd']
               y.set_password(password)
               y.first_name = request.data['fname']
               y.last_name = request.data['lname']
               y.email = request.data['mail']

               x.save()
               y.save()

               datas={
                    "USERNAME" : x.username,
                    "PASSWORD" : y.password,
                    "FIRST NAME" : x.first_name,
                    "LAST NAME" : y.last_name,
                    "GENDER": x.gender,
                    "PHONE" : x.phone,
                    "EMAIL" : x.email,
                    "PLACE" : x.place,
                    "PHOTO" : x.photo,
                    "ADDRESS" : x.address
               }
          except Exception as e:
               return failure_response(response)
          
          response={}
          response['is Success'] = True
          response['Status messege'] = 'successfully done'
          response['DATA'] = datas
          return success_response(response)

class auth_login(APIView):
     def post(self,request):
          datas={}
          response={}

          try:
               username=request.data['user']
               password=request.data['pwd']
               print("helo")
               d=authenticate( username=username,password=password)
               print(d,'test1')
               a=tbl_user1.objects.get(username=d)
               if d is not None:
                    data={
                        "USERNAME" : d.username,
                    "PASSWORD" : d.password,
                    "FIRST NAME" : d.first_name,
                    "LAST NAME" : d.last_name,
                    "GENDER": a.gender,
                    "PHONE" : a.phone,
                    "EMAIL" : d.email,
                    "PLACE" : a.place,
                    "PHOTO" : a.photo,
                    "ADDRESS" : a.address
                    }
               else:
                    response['messege']='user does not exist'
                    return failure_response(response)
          except Exception as e:
                    response["statusMessage"]='user does not exist'
                    return failure_response(response)

          response['isSuccess'] = True
          response["statusMessage"]='successfully done'
          response["DATA"]=data   
          return success_response(response)
     
class viewaccount(APIView):
     def get(self,request):
          p1= tbl_user1.objects.all()
          info=[]
          if p1 is not None:
               for x in p1:
                    datas={
                          "USERNAME" : x.username,
          
                    "FIRST NAME" : x.first_name,
          
                    "GENDER": x.gender,
                    "PHONE" : x.phone,
                    "EMAIL" : x.email,
                    "PLACE" : x.place,
                    "PHOTO" : x.photo,
                    "ADDRESS" : x.address
                    }
                    info.append(datas)
                    response={}
                    response['is Success'] = True
                    response['Status messege'] = 'successfully done'
                    response['DATA'] = datas
                    return success_response(response)
               
          else:
               return failure_response(response)

class delete_user(APIView):
     def post(self,request):
          data={}
          response={}

          a = request.data['e_id']
          try:
               x = tbl_user1.objects.get(id=a)
               if x:
                    x.delete()
               else:
                    response['messege'] = 'user does not exist'
                    return failure_response(response)
               
          except Exception as e:
                    response["statusMessage"]='user does not exist'
                    return failure_response(response)

          response['isSuccess'] = True
          response["statusMessage"]='successfully done'
          response["DATA"]=data   
          return success_response(response)

class update_user(APIView):
     def post(self,request):
          datas={}
          response={}

          a = request.data['user_id']
          print('test1',a)
          try:
          
               y = tbl_user1.objects.get(id = a)
               if y:
                    y.username = request.data['user']
                    y.first_name = request.data['fname']
                    y.gender = request.data['gender']
                    y.phone = request.data['ph']
                    y.email = request.data['mail']
                    y.place = request.data['place']
                    y.photo = request.FILES['photo']
                    y.address = request.data['adrs']

                    y.save()

               else:
                    response['messege'] = 'user does not exist'
                    return failure_response(response)
          except Exception as e:
                    response["statusMessage"]='user does not exist'
                    return failure_response(response)

          response['isSuccess'] = True
          response["statusMessage"]='successfully done'
          response["DATA"]=datas  
          return success_response(response)
     
class addproduct(APIView):
     def post(self,request):

          datas={}
          response={}

          try:
               user = tbl_products()

               user.product_name = request.data['product']
               user.price = request.data['rs']
               user.color = request.data['color']
               user.warranty = request.data['warranty']
               user.photo = request.data['profileimage']
               user.save()

               datas={
                    "PRODUCT NAME " : user.product_name,
                    "PRICE" : user.price,
                    "COLOR" : user.color,
                    "WARRANTY" : user.warranty,
                    "PHOTO" : user.photo,
               }
          except Exception as e:
               return failure_response(response)
        
          response={}
          response['isSuccess'] = True
          response["statusMessage"]='successfully done'
          response["DATA"]=datas
          return success_response(response) 
     
class viewproduct(APIView):
     def get(self,request):
          p1= tbl_products.objects.all()
          info=[]
          try:

               if p1 is not None:
                    for x in p1:
                         datas={
                              "PRODUCT NAME" : x.product_name,
                              "PRICE": x.price,
                              "COLOR" : x.color,
                              "WARRANTY" : x.warranty,
                              "PHOTO" : x.photo,
                    
                    }
                         info.append(datas)
                    
               
               else:
                    return failure_response(response)
               
          except Exception as e:
               return failure_response(response)
        
          response={}
          response['isSuccess'] = True
          response["statusMessage"]='successfully done'
          response["DATA"]=info
          return success_response(response) 
     
          
class delete_product(APIView):
     def post(self,request):
          data={}
          response={}

          a = request.data['e_id']
          try:
               x = tbl_products.objects.get(id=a)
               if x:
                    x.delete()
               else:
                    response['messege'] = 'product does not exist'
                    return failure_response(response)
               
          except Exception as e:
                    response["statusMessage"]='product does not exist'
                    return failure_response(response)

          response['isSuccess'] = True
          response["statusMessage"]='successfully done'
          response["DATA"]=data   
          return success_response(response)
     
class update_product(APIView):
     def post(self,request):
          datas={}
          response={}

          a = request.data['user_id']
          try:
               y = tbl_products.objects.get(id = a)
               if y:
                    y.product_name = request.data['product']
                    y.price = request.data['rs']
                    y.color = request.data['color']
                    y.warranty = request.data['warranty']
                    y.photo = request.data['profileimage']
                   
                    y.save()
               else:
                    response['messege'] = 'user does not exist'
                    return failure_response(response)
          except Exception as e:
                    response["statusMessage"]='user does not exist'
                    return failure_response(response)

          response['isSuccess'] = True
          response["statusMessage"]='successfully done'
          response["DATA"]=datas  
          return success_response(response)
     
class product1(APIView):
     def get(self,request):
     
          p1= tbl_products.objects.filter(price__lte = 5000)
          info=[]
          try:

               if p1 is not None:
                    for x in p1:
                         datas={
                              "PRODUCT NAME" : x.product_name,
                              "PRICE": x.price,
                              "COLOR" : x.color,
                              "WARRANTY" : x.warranty,
                              "PHOTO" : x.photo,
                    
                    }
                         info.append(datas)
                    
               
               else:
                    return failure_response(response)
               
          except Exception as e:
               return failure_response(response)
        
          response={}
          response['isSuccess'] = True
          response["statusMessage"]='successfully done'
          response["DATA"]=info
          return success_response(response) 
     

class mobile(APIView):
     def get(self,request):
     
          p1= tbl_products.objects.filter(product_name = "mobile")
          info=[]
          try:

               if p1 is not None:
                    for x in p1:
                         datas={
                              "PRODUCT NAME" : x.product_name,
                              "PRICE": x.price,
                              "COLOR" : x.color,
                              "WARRANTY" : x.warranty,
                              "PHOTO" : x.photo,
                    
                    }
                         info.append(datas)
                    
               
               else:
                    return failure_response(response)
               
          except Exception as e:
               return failure_response(response)
        
          response={}
          response['isSuccess'] = True
          response["statusMessage"]='successfully done'
          response["DATA"]=info
          return success_response(response) 
     