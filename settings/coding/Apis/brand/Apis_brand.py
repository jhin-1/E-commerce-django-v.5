from rest_framework.response import Response
from rest_framework.decorators import api_view
from settings.coding.Oop_brand.Oop_brand import *


@api_view(["GET"])
def all_(request):
    call = BrandOop(request).all()
    re_status, re_massage, re_data, page = call[0], call[1], call[2], call[3]
    re_send = {
        "massage": re_massage,
        "data": re_data,
        "page": int(page) if page else "",
    }
    return Response(re_send, re_status)


@api_view(["GET"])
def open_brand(request):
    call = BrandOop(request).open()
    re_status, re_massage, re_data,  = call[0], call[1], call[2]
    re_send = {
        "massage": re_massage,
        "data": re_data,
    }
    return Response(re_send, re_status)


@api_view(["POST"])
def create_brand(request):
    call = BrandOop(request).create()
    re_status, re_massage, re_data,  = call[0], call[1], call[2]
    re_send = {
        "massage": re_massage,
        "data": re_data,
    }
    return Response(re_send, re_status)


@api_view(["DELETE"])
def delete_brand(request):
    call = BrandOop(request).delete()
    re_status, re_massage,   = call[0], call[1],
    re_send = {
        "massage": re_massage,
    }
    return Response(re_send, re_status)