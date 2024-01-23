from rest_framework.response import Response
from rest_framework.decorators import api_view
from ...Oop_category.category_oop import *


@api_view(['GET'])
def all_category(request):
    call = CategoryOops(request).all_category()
    re_status, re_massage, re_data = call[0], call[1], call[2]
    re_send = {
        "massage": re_massage,
        "data": re_data,
    }
    return Response(re_send, re_status)