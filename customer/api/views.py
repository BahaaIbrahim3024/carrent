from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import  CustomerSerializer
from customer.models import Customer


class CustomerList(APIView):
    def get(self, request, id):
        try:
            customers = Customer.objects.get(pk=id)
        except Customer.DoesNotExist:
            Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = CustomerSerializer(customers)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        try:
            customer = Customer.objects.get(pk=id)
        except Customer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'PUT':
            ser = CustomerSerializer(customer, request.data, partial=True)
            data = {}
            if ser.is_valid():
                ser.save()
                data['success'] = 'Customer data updated successful'
                return Response(data=data)
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        if request.method == 'POST':
            serializer = CustomerSerializer(data=request.data)
            data = {}
            if serializer.is_valid():
                customer = serializer.save()
                data['response'] = 'a New Customer added'
                data['email'] = customer.email
                data['name'] = customer.name
                data['phone'] = customer.phone
                data['address'] = customer.address
                data['gender'] = customer.gender
                data['status'] = customer.status
            else:
                data['response'] = serializer.errors
            return Response(data)

    def delete(self, request, id):
            try:
                customer = Customer.objects.get(pk=id)
            except Customer.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            if request.method == 'DELETE':
                operation = customer.delete()
                data = {}
                if operation:
                    data['success'] = 'Delete Success'
                else:
                    data['fail'] = 'Delete Fail'
                return Response(data=data)
