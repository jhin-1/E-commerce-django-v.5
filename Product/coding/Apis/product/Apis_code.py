from rest_framework.response import Response
from rest_framework.decorators import api_view
from Product.coding.Oop_product.oop_code_product import *


@api_view(['GET'])
def all_product(request):
    call = ProductOops(request).all()
    re_status, re_message, re_data, page = call[0], call[1], call[2], call[3]
    re_send = {
        "message": re_message,
        "data": re_data,
        "page": int(page),
    }
    return Response(re_send, re_status)


@api_view(['GET'])
def open_product(request):
    call = ProductOops(request).open()
    re_status, re_massage, re_data = call[0], call[1], call[2]
    re_send = {
        "massage": re_massage,
        "data": re_data,
    }
    return Response(re_send, re_status)


@api_view(['POST'])
def create_product(request):
    call = ProductOops(request).create_product()
    re_status, re_massage, re_data = call[0], call[1], call[2]
    re_send = {
        "massage": re_massage,
        "data": re_data,
    }
    return Response(re_send, re_status)


@api_view(["PUT"])
def update_product(request):
    call = ProductOops(request).update_product()
    re_status, re_massage, re_data = call[0], call[1], call[2]
    re_send = {
        "massage": re_massage,
        "data": re_data,
    }
    return Response(re_send, re_status)


@api_view(["DELETE"])
def delete_product(request):
    call = ProductOops(request).delete_product()
    re_status, re_massage = call[0], call[1]
    re_send = {
        "massage": re_massage,
    }
    return Response(re_send, re_status)