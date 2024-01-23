# from ...models import *
# from rest_framework import status
# from django.core.paginator import Paginator
#
#
# class CategoryOops:
#     def __init__(self, request):
#         self.request = request
#         self.list_items = []
#         self.re_status, self.re_massege, self.re_data = status.HTTP_404_NOT_FOUND, "", None
#         self.page_number = self.request.GET.get("page", 1)  # تعيين قيمة افتراضية
#         try:
#             self.name = self.request.POST.get("name")
#         except:
#             self.name = None
#         try:
#             self.cat_parent = Category.objects.get(id=self.request.POST.get("id_cat_parent"))
#         except:
#             self.cat_parent = None
#         try:
#             self.description = self.request.POST.get("description")
#         except:
#             self.description = None
#         try:
#             self.image = self.request.POST.get("image")
#         except:
#             self.image = None
#
#     # def all_category(self):
#     #     category = Paginator(Category.objects.all(), 3).get_page(self.page_number)
#     #     if category:
#     #         for category in category:
#     #             category = {
#     #                 'id_category': category.id,
#     #                 'name': category.name,
#     #                 'cat_parent': category.name if category.cat_parent else None,
#     #                 'description': category.description,
#     #                 # 'image': category.image,
#     #             }
#     #             self.list_items.append(category)
#     #             self.re_status = status.HTTP_200_OK
#     #             self.re_massege = "ok"
#     #             self.re_data = self.list_items
#     #     else:
#     #         self.re_status = status.HTTP_404_NOT_FOUND
#     #         self.re_massege = "not found"
#     #         self.re_data = None
#     #     return [self.re_status, self.re_massege, self.re_data]