from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CartItemSerializer
from .models import CartItem


class CartItemView(APIView):

    def get(self, request, id=None):
        if id:
            item = CartItem.objects.get(id=id)
            serializer = CartItemSerializer(item)
            return Response({'status': 'Success', "data": serializer.data}, status=status.HTTP_200_OK)

        items = CartItem.objects.all()
        serializer = CartItemSerializer(items, many=True)
        return Response({'status': 'Success', "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'Success', "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'error', "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        item = CartItem.objects.get(id=id)
        serializer = CartItemSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'Success', "data": serializer.data}, status=status.HTTP_200_OK)

        return Response({'status': 'error', "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        item = CartItem.objects.get(id=id)
        item.delete()
        return Response({'status': 'Success', "data": "Item Deleted"}, status=status.HTTP_200_OK)
