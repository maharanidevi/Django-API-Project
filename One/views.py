from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import Users, Orders, Products
from . serializers import Orders_serializer, Product_serializer, Users_serializer



class UserApi(APIView):

    # def get(self, request):
    #     all_users= Users.objects.all()
       

    #     data = []
    #     for u in all_users:
    #         data.append({
    #             "id":u.id,
    #             "name": u.UserName,
    #             "email": u.email,
    #             "password": u.password
    #         })

    #     return Response(data)
    def get(self,request):
        all_users = Users.objects.all()
        serializer = Users_serializer(all_users, many=True)  
        return Response(serializer.data) 
    
        

    # def post (self, request):
    #     print(request.data)
    #     new_user= Users(UserName= request.data['name'], email= request.data['email'],password=request.data['password'])
    #     new_user.save()
    #     return Response ("User created")
    def post(self, request):
        new_user = Users_serializer(data=request.data)
        if new_user.is_valid():
            new_user.save()
            return Response("New User Added")
            
        else:
            return Response(new_user.errors)
  


    # def patch(self, request, user_id):
    #     user_data= Users.objects.filter(id=user_id)

    #     user_data.update(UserName= request.data['name'], email= request.data['email'],password=request.data['password'])
       
    #     return Response("Update Users")
    def patch(self, request, user_id):

        user = Users.objects.get(id=user_id)

        serializer = Users_serializer(user, data=request.data, partial=True)

        if serializer.is_valid():
             serializer.save()
             return Response("User Updated Successfully")
        else:
             return Response(serializer.errors)


    # def put(self, request, user_id):
    #     user_data= Users.objects.filter(id=user_id)

    #     user_data.update(UserName= request.data['name'], email= request.data['email'],password=request.data['password'])
       
    #     return Response("Update Users using put")
    
    # def delete(self, request, user_id):
    #     user_data= Users.objects.get(id= user_id)
    #     user_data.delete()
    #     return Response(" User Data Deleted")
    def delete(self, request, order_id):
        users= Users.objects.filter(id=order_id)
        if users.exists():
            users.delete()
            return Response("User Deleted")
        else:
            return Response("User Is Not Found")
    


class OrderApi(APIView) :


    def get(self, request):
        all_orders = Orders.objects.all()                 
        serializer = Orders_serializer(all_orders, many=True)  
        return Response(serializer.data) 
    
    def post(self, request):
        new_order = Orders_serializer(data=request.data)
        if new_order.is_valid():
            new_order.save()
            return Response("New Order Added")
            
        else:
            return Response(new_order.errors)
        
    def patch(self, request, order_id):

        order = Orders.objects.get(id=order_id)

        serializer = Orders_serializer(order, data=request.data, partial=True)

        if serializer.is_valid():
             serializer.save()
             return Response("Order Updated Successfully")
        else:
             return Response(serializer.errors)

    def delete(self, request, order_id):
        orders= Orders.objects.filter(id=order_id)
        if orders.exists():
            orders.delete()
            return Response("Order Deleted")
        else:
            return Response("Order Is Not Found")
    
 
class ProductApi(APIView):


    def get(self,request):
        all_products=Products.objects.all()
        serializer=Product_serializer(all_products,many=True)
        return Response(serializer.data)


    
    def post(self,request):
        new_product= Product_serializer(data=request.data)
        if new_product.is_valid():
            new_product.save()
            return Response("new_product added")
        else:
            return Response (new_product.errors)
        
    def patch(self, request, id):
        
        product = Products.objects.get(id=id)

        serializer = Product_serializer(product, data=request.data, partial=True)

        if serializer.is_valid():
             serializer.save()
             return Response("Product Updated Successfully")
        else:
             return Response(serializer.errors)
        

    def delete(self, request, id):
        products=Products.objects.filter(id= id)
        if products.exists():
            products.delete()
            return Response("Product Deleted Successfully")
        else:
            return Response("Product Not Found")
