from Product.coding.Cart.Oop_cart import *
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(["PUT"])
def add_pro_cart_to(request):
    call = AddCart(request).add_to_cart()
    re_status, re_massage, re_data = call[0], call[1], call[2]
    re_send = {
        "massage": re_massage,
        "data": re_data,
    }
    return Response(re_send, re_status)