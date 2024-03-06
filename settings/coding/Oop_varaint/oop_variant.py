from ...models import *
# from Product.coding.Oop_product.oop_code_product import *
from rest_framework import status
from django.core.paginator import Paginator, EmptyPage


class ColorOop:
    def __init__(self, request):
        self.request = request
        self.list_items = []
        self.re_status, self.re_massege, self.re_data = status.HTTP_404_NOT_FOUND, "", None
        try:
            self.color = Color.objects.get(id=self.request.POST.get("id_color"))
        except:
            self.color = None
        try:
            self.size = Size.objects.get(id=self.request.POST.get("id_size"))
        except:
            self.size = None
        try:
            self.get_color = Color.objects.get(id=self.request.GET.get("id_color"))
        except:
            self.get_color = None
        try:
            self.name = self.request.POST.get("name")
        except:
            self.name = None
        try:
            self.code_color = int(self.request.POST.get("code_color"))
        except:
            self.code_color = 0
        try:
            self.quantity = int(self.request.POST.get("quantity"))
        except:
            self.quantity = 0
        try:
            self.price = int(self.request.POST.get("price"))
        except:
            self.price = 0
        try:
            self.page = int(self.request.GET.get("page"))  # تعيين قيمة افتراضية
        except:
            self.page = 1
        self.total_pages = 0
        self.all_items = []

    def pagination_return(self):
        all_items_ = Paginator(self.all_items, 4)
        try:
            self.list_items = all_items_.page(self.page)
        except EmptyPage:
            self.list_items = []
        self.total_pages = int(all_items_.num_pages)
        self.re_status = status.HTTP_200_OK
        self.re_data = {
            'list_items': list(self.list_items),
            'page': self.page,
            'total_pages': self.total_pages,
        }

    def all_color(self):
        all_color = Color.objects.all()
        for color in all_color:
            color_info = {
                "id": color.id,
                "name": color.name,
            }
            self.all_items.append(color_info)
        self.pagination_return()
        self.re_massege = "success"
        return [self.re_status, self.re_massege, self.re_data]

    def open_color(self):
        try:
            color_info = Color.objects.get(id=self.request.GET.get('id_color'))
        except:
            color_info = None
        if color_info:
            self.re_data = {
                "id": color_info.id,
                "name": color_info.name,
                "code-color": int(color_info.code_color),
            }
            self.re_status = status.HTTP_200_OK
            self.re_massege = "opened"
        else:
            self.re_status = status.HTTP_404_NOT_FOUND
            self.re_massege = "not found"
        return [self.re_status, self.re_massege, self.re_data]

    def check_input_color(self):  # validate inputs
        self.re_status = status.HTTP_400_BAD_REQUEST
        self.re_massege = "bad request"
        if self.name is None or self.name == "":
            self.re_massege = "please enter a name"
        elif len(self.name) <= 3:
            self.re_massege = "The minimum number of characters 4"
        elif len(self.name) >= 30:
            self.re_massege = "The maximum number of characters 29"
        elif self.code_color == 0:
            self.re_massege = "Please enter the code of color"
        elif self.code_color <= 1:
            self.re_massege = "The minimum number of code color is 1"
        elif self.code_color >= 60:
            self.re_massege = "The maximum number of code color is 59"
        else:
            self.re_status = status.HTTP_100_CONTINUE
            self.re_massege = " CONTINUE"

    def create_color(self):
        self.check_input_color()
        if self.re_status == status.HTTP_100_CONTINUE:
            try:
                create_color = Color.objects.create(name=self.name, code_color=self.code_color)
                if create_color:
                    self.re_data = {
                        "id": create_color.id,
                        "title": create_color.name,
                        "code_color": create_color.code_color,
                    }
                    self.re_status = status.HTTP_201_CREATED
                    self.re_massege = "created successfully"
                else:
                    self.re_status = status.HTTP_400_BAD_REQUEST
                    self.re_massege = "cant create"
            except Exception as e:
                self.re_status = status.HTTP_500_INTERNAL_SERVER_ERROR
                self.re_massege = str(e)
                self.re_data = None
        return [self.re_status, self.re_massege, self.re_data]

    def update_color(self):
        self.check_input_color()
        if self.re_status == status.HTTP_100_CONTINUE:
            try:
                update_color = self.color
                if update_color:
                    update_color.name = self.name
                    update_color.code_color = self.code_color
                    update_color.save()
                    self.re_status = status.HTTP_200_OK
                    self.re_massege = "Updated color"
                    self.re_data = {
                        "id": update_color.id,
                        "title": update_color.name,
                        "code_color": update_color.code_color,
                    }
                else:
                    self.re_status = status.HTTP_404_NOT_FOUND
                    self.re_massege = "Not Found"
            except Exception as e:
                self.re_status = status.HTTP_500_INTERNAL_SERVER_ERROR
                self.re_massege = str(e)
                self.re_data = None

        return [self.re_status, self.re_massege, self.re_data]

    def delete_color(self):
        delete = self.color
        if delete:
            delete.delete()
            self.re_status = status.HTTP_200_OK
            self.re_massege = "Deleted color"
        else:
            self.re_status = status.HTTP_404_NOT_FOUND
            self.re_massege = "Not found"
        return [self.re_status, self.re_massege]


class SizeOop(ColorOop):
    def all_size(self):
        all_size = Size.objects.all()
        for size in all_size:
            info_size = {
                "id": size.id,
                "name": size.name,
            }
            self.all_items.append(info_size)
        self.pagination_return()
        self.re_massege = "success"
        return [self.re_status, self.re_massege, self.re_data]

    def open_size(self):
        try:
            size = Size.objects.get(id=self.request.GET.get('id_size'))
        except:
            size = None
        if size:
            self.re_status = status.HTTP_200_OK
            self.re_massege = "successfully opened"
            self.re_data = {
                "id": size.id,
                "name": size.name,
            }
        else:
            self.re_status = status.HTTP_404_NOT_FOUND
            self.re_massege = "Not Found"
            self.re_data = None
        return [self.re_status, self.re_massege, self.re_data]

    def create_size(self):
        try:
            create_size = Size.objects.create(name=self.name)
            if create_size:
                self.re_status = status.HTTP_201_CREATED
                self.re_massege = "created"
                self.re_data = {
                    "id": create_size.id,
                    "name": create_size.name,
                }
            else:
                self.re_status = status.HTTP_400_BAD_REQUEST
                self.re_massege = "cannot create"
                self.re_data = None
        except Exception as e:
            self.re_status = status.HTTP_500_INTERNAL_SERVER_ERROR
            self.re_massege = str(e)
            self.re_data = None
        return [self.re_status, self.re_massege, self.re_data]

    def update_size(self):
        try:
            update_size = Size.objects.get(id=self.request.POST.get("id_size"))
        except:
            update_size = None
        if update_size:
            update_size.name = self.name
            update_size.save()
            self.re_status = status.HTTP_200_OK
            self.re_massege = "Updated"
            self.re_data = {
                "id": update_size.id,
                "name": update_size.name,
            }
        else:
            self.re_status = status.HTTP_404_NOT_FOUND
            self.re_massege = "Not Found"
            self.re_data = None
        return [self.re_status, self.re_massege, self.re_data]

    def delete_size(self):
        delete_size = Size.objects.get(id=self.request.POST.get("id_size"))
        if delete_size:
            delete_size.delete()
            self.re_status = status.HTTP_200_OK
            self.re_massege = "Deleted successfully"
        else:
            self.re_status = status.HTTP_404_NOT_FOUND
            self.re_massege = " Not Found!!"
        return [self.re_status, self.re_massege]


class VariantOop(SizeOop):
    def all_variant(self):
        all_variants = Variant.objects.all()
        for v in all_variants:
            variant = {
                "id": v.id,
                "color": v.color.name,
                "size": v.size.name,
            }
            self.all_items.append(variant)
        self.pagination_return()
        self.re_massege = " succeed"
        return [self.re_status, self.re_massege, self.re_data]

    def open_variant(self):
        try:
            variant = Variant.objects.get(id=self.request.GET.get('id_variant'))
        except:
            variant = None
        if variant:
            self.re_status = status.HTTP_200_OK
            self.re_massege = "Opened Successfully"
            self.re_data = {
                "id": variant.id,
                "Color_info": [
                    {
                        "id": variant.color.id,
                        "name": variant.color.name,
                        "code_color": variant.color.code_color,
                    }
                ],
                "size_info": [
                    {
                        "id": variant.size.id,
                        "name": variant.size.name,
                    }
                ],
                "quantity": variant.quantity,
                "price": variant.price,
            }
        else:
            self.re_status = status.HTTP_404_NOT_FOUND
            self.re_massege = "Not Found"
            self.re_data = None
        return [self.re_status, self.re_massege, self.re_data]

    def check_input_variant(self):
        self.re_status = status.HTTP_404_NOT_FOUND
        self.re_massege = "BAD REQUEST"
        if self.color == 0 or self.color == "":
            self.re_massege = "please enter the id of color"
        elif self.size == 0 or self.size == "":
            self.re_massege = "please enter The id of size"
        elif self.quantity == 0:
            self.re_massege = "please enter The quantity of the variant"
        elif self.quantity >= 50:
            self.re_massege = "please maximum number of variants 49"
        elif self.price == 0:
            self.re_massege = "please enter the price of the variant"
        elif self.price >= 50:
            self.re_massege = "The maximum price of the variant is 49"
        else:
            self.re_status = status.HTTP_100_CONTINUE
            self.re_massege = "CONTINUE"

    def create_variant(self):
        self.check_input_variant()
        if self.re_status == status.HTTP_100_CONTINUE:
            try:
                create_variant = Variant.objects.create(
                    color=self.color,
                    size=self.size,
                    quantity=self.quantity,
                    price=self.price,
                )
                self.re_status = status.HTTP_201_CREATED
                self.re_massege = "created successfully"
                self.re_data = {
                    "id": create_variant.id,
                    "color_info": [
                        {
                            "id": create_variant.color.id,
                            "name": create_variant.color.name,
                            "code_color": create_variant.color.code_color,
                        }
                    ],
                    "size_info": [
                        {
                            "id": create_variant.size.id,
                            "name": create_variant.size.name,
                        }
                    ],
                    "quantity": create_variant.quantity,
                    "price": create_variant.price,
                }
            except Exception as e:
                self.re_status = status.HTTP_500_INTERNAL_SERVER_ERROR
                self.re_massege = str(e)
                self.re_data = None
        return [self.re_status, self.re_massege, self.re_data]

    def update_variant(self):
        self.check_input_variant()
        if self.re_status == status.HTTP_100_CONTINUE:
            try:
                update_variant = Variant.objects.get(id=self.request.POST.get("id_variant"))
                if update_variant:
                    update_variant.color = self.color
                    update_variant.size = self.size
                    update_variant.quantity = self.quantity
                    update_variant.price = self.price
                    update_variant.save()
                    self.re_status = status.HTTP_200_OK
                    self.re_massege = "Updated Successfully"
                    self.re_data = {
                        "id": update_variant.id,
                        "color_info": [
                            {
                                "id": update_variant.color.id,
                                "name": update_variant.color.name,
                                "code_color": update_variant.color.code_color,
                            }
                        ],
                        "size_info": [
                            {
                                "id": update_variant.size.id,
                                "name": update_variant.size.name,
                            }
                        ],
                        "quantity": update_variant.quantity,
                        "price": update_variant.price,
                    }
            except Exception as e:
                self.re_status = status.HTTP_500_INTERNAL_SERVER_ERROR
                self.re_massege = str(e)
                self.re_data = None
        return [self.re_status, self.re_massege, self.re_data]

    def delete_variant(self):
        try:
            delete_variant = Variant.objects.get(id=self.request.POST.get('id_variant'))
        except:
            delete_variant = None
        if delete_variant:
            delete_variant.delete()
            self.re_status = status.HTTP_200_OK
            self.re_massege = "Deleted Successfully"
        else:
            self.re_status = status.HTTP_404_NOT_FOUND
            self.re_massege = "Not Found"
        return [self.re_status, self.re_massege]
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
#           self.re_status      = status.HTTP_404_NOT   found
