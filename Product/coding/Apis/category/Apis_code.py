from rest_framework.response import Response
from rest_framework.decorators import api_view
from Product.coding.Oop_category.category_oop import *


@api_view(['GET'])  # added pagination for the request all
def all_category(request):
    call = MainCategory(request).all_m_category()
    re_status, re_massage, re_data, page = call[0], call[1], call[2], call[3]
    re_send = {
        "massage": re_massage,
        "data": re_data,
        "page": int(page) if page else 1,
        }

    return Response(re_send, re_status)


@api_view(["GET"])
def opem_m_category(request):
    call = MainCategory(request).open_m_category()
    re_status, re_massage, re_data = call[0], call[1], call[2]
    re_send = {
        "massage": re_massage,
        "data": re_data,
    }
    return Response(re_send, re_status)


@api_view(["POST"])
def create_m_category(request):
    call = MainCategory(request).create_m_category()
    re_status, re_massage, re_data = call[0], call[1], call[2]
    re_send = {
        "massage": re_massage,
        "data": re_data,
    }
    return Response(re_send, re_status)


@api_view(["PUT"])
def update_m_category(request):
    call = MainCategory(request).update_m_category()
    re_status, re_massage, re_data = call[0], call[1], call[2]
    re_send = {
        "massage": re_massage,
        "data": re_data,
    }
    return Response(re_send, re_status)


@api_view(["DELETE"])
def delete_m_category(request):
    call = MainCategory(request).delete_m_category()
    re_status, re_massage, re_data = call[0], call[1], call[2]
    re_send = {
        "massage": re_massage,
        "data": re_data,
    }
    return Response(re_send, re_status)


@api_view(["GET"])
def all_s_category(request):
    call = SubCategoryOop(request).all_s_category()
    re_status, re_massage, re_data = call[0], call[1], call[2]
    re_send = {
        "massage": re_massage,
        "data": re_data,
    }
    return Response(re_send, re_status)


@api_view(["GET"])
def open_s_category(request):
    call = SubCategoryOop(request).open_s_category()
    re_status, re_massage, re_data = call[0], call[1], call[2]
    re_send = {
        "massage": re_massage,
        "data": re_data,
    }
    return Response(re_send, re_status)


@api_view(["POST"])
def create_s_category(request):
    call = SubCategoryOop(request).create_s_category()
    re_status, re_massage, re_data = call[0], call[1], call[2]
    re_send = {
        "massage": re_massage,
        "data": re_data,
    }
    return Response(re_send, re_status)


@api_view(["PUT"])
def update_s_category(request):
    call = SubCategoryOop(request).update_s_category()
    re_status, re_massage, re_data = call[0], call[1], call[2]
    re_send = {
        "massage": re_massage,
        "data": re_data,
    }
    return Response(re_send, re_status)


@api_view(["DELETE"])
def delete_s_category(request):
    call = SubCategoryOop(request).delete_s_category()
    re_status, re_massage = call[0], call[1]
    re_send = {
        "massage": re_massage,
    }
    return Response(re_send, re_status)