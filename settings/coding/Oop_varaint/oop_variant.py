from ...models import *
# from Product.coding.Oop_product.oop_code_product import *
from rest_framework import status
from django.core.paginator import Paginator, EmptyPage


# class ColorOop:
#     def __init__(self, request):
#         self.request = request
#         self.list_items = []
#         self.re_status, self.re_massege, self.re_data = status.HTTP_404_NOT_FOUND, "", None
#         try:
#             self.color = Color.objects.get(id=self.request.POST.get("id_color"))
#         except:
#             self.color = None
#         try:
#             self.title = self.request.POST.get("title")
#         except:
#             self.title = None
#         try:
#             self.code_color = int(self.request.POST.get("code_color"))
#         except:
#             self.code_color = 0
#         try:
#             self.page = int(self.request.GET.get("page"))  # تعيين قيمة افتراضية
#         except:
#             self.page = 1
#         self.total_pages = 0
#         self.all_items = []
#
#     def pagination_return(self):
#         all_items_ = Paginator(self.all_items, 3)
#         try:
#             self.list_items = all_items_.page(self.page)
#         except EmptyPage:
#             self.list_items = []
#         self.total_pages = int(all_items_.num_pages)
#         self.re_status = status.HTTP_200_OK
#         self.re_data = {
#             'list_items': list(self.list_items),
#             'page': self.page,
#             'total_pages': self.total_pages,
#         }
#
#     def all_color(self):
#         all_color = Color.objects.all()
#         for color in all_color:
#             color_info = {
#                 "id": color.id,
#                 "name": color.title,
#             }
#             self.all_items.append(color_info)
#         self.pagination_return()
#         return [self.re_status, self.re_massege, self.re_data]
#
#     def open_color(self):
#         try:
#             color_info = Color.objects.get(id=self.request.GET.get('id_color'))
#         except:
#             color_info = None
#         if color_info:
#             self.re_data = {
#                 "id": color_info.id,
#                 "name": color_info.title,
#                 "code-color": color_info.code_color,
#             }
#             self.re_status = status.HTTP_200_OK
#             self.re_massege = "opened"
#         else:
#             self.re_status = status.HTTP_404_NOT_FOUND
#             self.re_massege = "not found"
#         return [self.re_status, self.re_massege, self.re_data]
#
#     def create_color(self):
#         try:
#             create_color = Color.objects.create(title=self.title, code_color=self.code_color)
#             if create_color:
#                 self.re_data = {
#                     "id": create_color.id,
#                     "title": create_color.title,
#                     "code_color": create_color.code_color,
#                 }
#                 self.re_status = status.HTTP_201_CREATED
#                 self.re_massege = "created successfully"
#             else:
#                 self.re_status = status.HTTP_400_BAD_REQUEST
#                 self.re_massege = "cant create"
#         except Exception as e:
#             self.re_status = status.HTTP_500_INTERNAL_SERVER_ERROR
#             self.re_massege = str(e)
#             self.re_data = None
#         return [self.re_status, self.re_massege, self.re_data]
#
#     def update_color(self):
#         try:
#             update_color = self.color
#             if update_color:
#                 update_color.title = self.title
#                 update_color.code_color = self.code_color
#                 update_color.save()
#                 self.re_status = status.HTTP_200_OK
#                 self.re_massege = "Updated color"
#                 self.re_data = {
#                     "id": update_color.id,
#                     "title": update_color.title,
#                     "code_color": update_color.code_color,
#                 }
#             else:
#                 self.re_status = status.HTTP_404_NOT_FOUND
#                 self.re_massege = "Not Found"
#         except Exception as e:
#             self.re_status = status.HTTP_500_INTERNAL_SERVER_ERROR
#             self.re_massege = str(e)
#             self.re_data = None
#
#         return [self.re_status, self.re_massege, self.re_data]
#
#     def delete_color(self):
#         delete = self.color
#         if delete:
#             delete.delete()
#             self.re_status = status.HTTP_200_OK
#             self.re_massege = "Deleted color"
#         else:
#             self.re_status = status.HTTP_404_NOT_FOUND
#             self.re_massege = "Not found"
#         return [self.re_status, self.re_massege]

# class VarOop:
#     def __init__(self, request):
#         self.request = request
#         self.list_items = []
#         self.re_status, self.re_massege, self.re_data = status.HTTP_404_NOT_FOUND, "", None
#         try:
#             self.title = self.request.POST.get('title')
#         except:
#             self.title = None
#         try:
#             self.var_1 = Var_1.objects.get(id=self.request.POST.get('id_var'))
#         except:
#             self.var_1 = None
#         try:
#             self.variant = Variant.objects.get(id=self.request.POST.get('id_variant'))
#         except:
#             self.variant = None
#         try:
#             self.name = self.request.POST.get('name')
#         except:
#             self.name = None
#         try:
#             self.page = int(self.request.GET.get("page"))  # تعيين قيمة افتراضية
#         except:
#             self.page = 1
#         self.total_pages = 0
#         self.all_items = []
#
#     def pagination_return(self):
#         all_itmes = Paginator(self.all_items, 3)
#         try:
#             self.list_items = all_itmes.page(self.page)
#         except EmptyPage:
#             self.list_items = []
#         self.total_pages = int(all_itmes.num_pages)
#         self.re_status = status.HTTP_200_OK
#         self.re_data = {
#             "list_items": list(self.list_items),
#             "page": self.page,
#             "total_pages": self.total_pages,
#         }
#
#     def all_var1(self):
#         all_var1 = Var_1.objects.all()
#         for var in all_var1:
#             var = {
#                 "ID": var.id,
#                 "title": var.title,
#             }
#             self.all_items.append(var)
#         self.pagination_return()
#         return [self.re_status, self.re_massege, self.re_data]
#
#     def open_var1(self):
#         try:
#             get_var1 = Var_1.objects.get(id=self.request.GET.get('id_var'))
#         except:
#             get_var1 = None
#         if get_var1:
#             self.re_status = status.HTTP_200_OK
#             self.re_massege = "opened successfully"
#             self.re_data = {
#                 "iD_var1": get_var1.id,
#                 "title": get_var1.title,
#             }
#         else:
#             self.re_status = status.HTTP_404_NOT_FOUND
#             self.re_massege = "Not found"
#             self.re_data = {}
#         return [self.re_status, self.re_massege, self.re_data ]
#
#     def create_var_1(self):
#         try:
#             create = Var_1.objects.create(title=self.title)
#             self.re_status = status.HTTP_201_CREATED
#             self.re_massege = "created successfully"
#             self.re_data ={
#                 "ID": create.id,
#                 "title": create.title,
#             }
#         except Exception as e:
#             self.re_status = status.HTTP_500_INTERNAL_SERVER_ERROR
#             self.re_massege = str(e)
#             self.re_data = None
#         return [self.re_status, self.re_massege, self.re_data]
#
#     def update_var_1(self):
#         try:
#             update_var1 = self.var_1
#         except:
#             update_var1 = None
#         if update_var1:
#             update_var1.title = self.title
#             update_var1.save()
#             self.re_status = status.HTTP_200_OK
#             self.re_massege = "UPDATED"
#             self.re_data ={
#                 "ID_VAR": update_var1.id,
#                 "title": update_var1.title,
#             }
#         else:
#             self.re_status = status.HTTP_400_BAD_REQUEST
#             self.re_massege = "Bad request"
#             self.re_data = None
#         return [self.re_status, self.re_massege, self.re_data]
#
#     def delete_var1(self):
#         try:
#             delete = self.var_1
#         except:
#             delete = None
#         if delete:
#             delete.delete()
#             self.re_status = status.HTTP_200_OK
#             self.re_massege = "deleted"
#         else:
#             self.re_status = status.HTTP_404_NOT_FOUND
#             self.re_massege = "Not found"
#         return [self.re_status, self.re_massege]
#
#
# class VariantOop(VarOop):
#
#     def all_variants(self):
#         all_variants = Variant.objects.all()
#         for v in all_variants:
#             v = {
#                 "id": v.id,
#                 "name": v.name,
#             }
#             self.all_items.append(v)
#         self.pagination_return()
#         return [self.re_status, self.re_massege, self.re_data]
#
#     def open_variant(self):
#         try:
#             get_info = Variant.objects.get(id=self.request.GET.get('id_variant'))
#         except:
#             get_info = None
#         if get_info:
#             self.re_status = status.HTTP_200_OK
#             self.re_massege = "OPENED SUCCESSFUL"
#             self.re_data = {
#                 "ID": get_info.id,
#                 "name": get_info.name,
#                 "var_1": [
#                     {
#                         "id_var_1": get_info.var_1.id,
#                         "title": get_info.var_1.title,
#                     }
#                 ]
#             }
#         else:
#             self.re_status = status.HTTP_404_NOT_FOUND
#             self.re_massege = "Not Found"
#             self.re_data = None
#         return [self.re_status, self.re_massege, self.re_data]
#
#     def check_inputs_validate(self):
#         self.re_status = status.HTTP_400_BAD_REQUEST
#         self.re_massege = "BAD REQUEST"
#         if self.name is None or self.name == "":
#             self.re_massege = "please enter the name "
#         elif len(self.name) <= 1:
#             self.re_massege = "the minimum character is 6"
#         elif len(self.name) >= 30:
#             self.re_massege = "the maximum character is 29"
#         else:
#             self.re_status = status.HTTP_100_CONTINUE
#             self.re_massege = " CONTINUE"
#
#     def create_variation(self):
#         self.check_inputs_validate()
#         if self.re_status == status.HTTP_100_CONTINUE:
#             try:
#                 create = Variant.objects.create(
#                     var_1=self.var_1,
#                     name=self.name,
#                 )
#                 self.re_status = status.HTTP_200_OK
#                 self.re_massege = "created successfully"
#                 self.re_data = {
#                     "ID": create.id,
#                     "Name": create.name,
#                     "var_1": [
#                         {
#                             "id_var": create.var_1.id,
#                             "title": create.var_1.title,
#                         }
#                     ]
#                 }
#             except Exception as e:
#                 self.re_status = status.HTTP_500_INTERNAL_SERVER_ERROR
#                 self.re_massege = str(e)
#                 self.re_data = None
#         return [self.re_status, self.re_massege, self.re_data]
#
#     def update_variation(self):
#         self.check_inputs_validate()
#         if self.re_status == status.HTTP_100_CONTINUE:
#             try:
#                 update = self.variant
#             except:
#                 update = None
#             if update:
#                 update.var_1 = self.var_1
#                 update.name = self.name
#                 update.quantity = self.quantity
#                 update.save()
#                 self.re_status = status.HTTP_200_OK
#                 self.re_massege = "UPDATED"
#                 self.re_data = {
#                     "ID": update.id,
#                     "name": update.name,
#                     "quantity": update.quantity,
#                     "var_1": [
#                         {
#                             "id-var": update.var_1.id,
#                             "title": update.var_1.title,
#                         }
#                     ]
#                 }
#             else:
#                 self.re_status = status.HTTP_404_NOT_FOUND
#                 self.re_massege = "Not Found"
#                 self.re_data = None
#             return [self.re_status, self.re_massege, self.re_data]
#
#     def delete_variant(self):
#         delete = self.variant
#         if delete:
#             delete.delete()
#             self.re_status = status.HTTP_200_OK
#             self.re_message = "deleted successfully"
#         else:
#             self.re_status = status.HTTP_404_NOT_FOUND
#             self.re_message = "not found"
#         return [self.re_status, self.re_message]
#
