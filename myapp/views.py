from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import User,Product,Category
from .serializer import Userserializers,ProductSerilzers,CategorySerializer


@api_view(['GET', 'POST'])
def get_user(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = Userserializers(users, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = Userserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['PUT'])
def update_user(request, pk):
    try:
        user = User.objects.get(id=pk)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=404)

    serializer = Userserializers(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def delete_user(request, pk):
    try:
        user = User.objects.get(id=pk)
        user.delete()
        return Response({'message': 'User deleted successfully'})
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=404)

@api_view(['GET'])
def product(request):
    if request.method == 'GET':
        product = Product.objects.all()
        serializer = ProductSerilzers(product,many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = ProductSerilzers(serializer.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors, status=400)

@api_view(['PUT'])
def update_product(request,pk):
    try:
        product = Product.objects.get(id= pk)
    except Product.DoesNotExist:
        return Response({'error': 'product not found'}, status=404)
    serializer = ProductSerilzers(product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delte_product(request,pk):
    try:
        product = Product.objects.get(id=pk)
        product.delete()
        return Response({'message': 'product deleted successfully'})
    except User.DoesNotExist:
       return Response({'error': 'product not found'}, status=404)
       

       
       
@api_view(['GET', 'POST'])
def category(request):
    if request.method == 'GET':
        category = Category.objects.all()
        serializer = CategorySerializer(category,many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = CategorySerializer(serializer.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors, status=400)


        
            

