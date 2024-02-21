from rest_framework.response import Response
from rest_framework.decorators import api_view
from settings.coding.Oop_varaint.oop_variant import *


# @api_view(["GET"])
# def all_color(request):
#     call = ColorOop(request).all_color()
#     re_status, re_message, re_data = call[0], call[1], call[2]
#     re_send = {
#         "message": re_message,
#         "data": re_data,
#     }
#     return Response(re_send, re_status)
#
#
# @api_view(["GET"])
# def open_color(request):
#     call = ColorOop(request).open_color()
#     re_status, re_message, re_data = call[0], call[1], call[2]
#     re_send = {
#         "message": re_message,
#         "data": re_data,
#     }
#     return Response(re_send, re_status)
#
#
# @api_view(["POST"])
# def create_color(request):
#     call = ColorOop(request).create_color()
#     re_status, re_message, re_data = call[0], call[1], call[2]
#     re_send = {
#         "message": re_message,
#         "data": re_data,
#     }
#     return Response(re_send, re_status)
#
#
# @api_view(["PUT"])
# def update_color(request):
#     call = ColorOop(request).update_color()
#     re_status, re_message, re_data = call[0], call[1], call[2]
#     re_send = {
#         "message": re_message,
#         "data": re_data,
#     }
#     return Response(re_send, re_status)
#
#
# @api_view(["DELETE"])
# def delete_color(request):
#     call = ColorOop(request).delete_color()
#     re_status, re_message = call[0], call[1]
#     re_send = {
#         "message": re_message,
#     }
#     return Response(re_send, re_status)

# @api_view(["GET"])
# def all_var1(request):
#     call = VarOop(request).all_var1()
#     re_status, re_message, re_data = call[0], call[1], call[2]
#     re_send = {
#         "message": re_message,
#         "data": re_data,
#     }
#     return Response(re_send, re_status)
#
#
# @api_view(["GET"])
# def open_var1(request):
#     call = VarOop(request).open_var1()
#     re_status, re_message, re_data = call[0], call[1], call[2]
#     re_send = {
#         "message": re_message,
#         "data": re_data,
#     }
#     return Response(re_send, re_status)
#
#
# @api_view(["POST"])
# def create_var1(request):
#     call = VarOop(request).create_var_1()
#     re_status, re_message, re_data = call[0], call[1], call[2]
#     re_send = {
#         "message": re_message,
#         "data": re_data,
#     }
#     return Response(re_send, re_status)
#
#
# @api_view(["PUT"])
# def update_var1(request):
#     call = VarOop(request).update_var_1()
#     re_status, re_message, re_data = call[0], call[1], call[2]
#     re_send = {
#         "message": re_message,
#         "data": re_data,
#     }
#     return Response(re_send, re_status)
#
#
# @api_view(["DELETE"])
# def delete_var1(request):
#     call = VarOop(request).delete_var1()
#     re_status, re_message,  = call[0], call[1]
#     re_send = {
#         "message": re_message,
#     }
#     return Response(re_send, re_status)
#
#
# @api_view(["GET"])
# def all_variant(request):
#     call = VariantOop(request).all_variants()
#     re_status, re_message, re_data = call[0], call[1], call[2]
#     re_send = {
#         "message": re_message,
#         "data": re_data,
#     }
#     return Response(re_send, re_status)
#
#
# @api_view(["GET"])
# def open_variant(request):
#     call = VariantOop(request).open_variant()
#     re_status, re_message, re_data = call[0], call[1], call[2]
#     re_send = {
#         "message": re_message,
#         "data": re_data,
#     }
#     return Response(re_send, re_status)
#
#
# @api_view(["POST"])
# def create_variant(request):
#     call = VariantOop(request).create_variation()
#     re_status, re_message, re_data = call[0], call[1], call[2]
#     re_send = {
#         "message": re_message,
#         "data": re_data,
#     }
#     return Response(re_send, re_status)
#
#
# @api_view(["PUT"])
# def update_variant(request):
#     call = VariantOop(request).update_variation()
#     re_status, re_message, re_data = call[0], call[1], call[2]
#     re_send = {
#         "message": re_message,
#         "data": re_data,
#     }
#     return Response(re_send, re_status)
#
#
# @api_view(["DELETE"])
# def delete_variant(request):
#     call = VariantOop(request).delete_variant()
#     re_status, re_message,  = call[0], call[1]
#     re_send = {
#         "message": re_message,
#     }
#     return Response(re_send, re_status)