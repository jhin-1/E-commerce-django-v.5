<<<<<<< HEAD
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
=======
from ...models import *
from rest_framework import status
from django.core.paginator import Paginator


class MainCategory:
    def __init__(self, request):
        self.request = request
        self.list_items = []
        self.re_status, self.re_massege, self.re_data = status.HTTP_404_NOT_FOUND, "", None
        self.page = self.request.GET.get("page", 1)  # تعيين قيمة افتراضية
        try:
            self.name = self.request.POST.get("name")
        except:
            self.name = None
        try:
            self.main_category = MainCategoryModel.objects.get(id=self.request.POST.get("id_main_category"))
        except:
            self.main_category = None
        try:
            self.sub_category = SubCategory.objects.get(id=self.request.POST.get("id_sub"))
        except:
            self.sub_category = None
        try:
            self.description = self.request.POST.get("description")
        except:
            self.description = None
        try:
            self.image = self.request.FILES.get("image", None)
        except:
            self.image = None
        self.main_exists = MainCategoryModelFilter(data=self.request.POST).qs
        self.sub_exists = SubCategoryFilter(data=self.request.POST).qs
    ''' add paginator if you have many objects you will returned it  example request all'''

    def all_m_category(self):
        m_category = Paginator(MainCategoryModel.objects.all(), 20).get_page(self.page)
        if m_category:
            for category in m_category:
                try:
                    image = category.image.url
                except:
                    image = ""
                category = {
                    'id_category': category.id,
                    'name': category.name,
                    'image': image,
                }
                self.list_items.append(category)
            self.re_status = status.HTTP_200_OK
            self.re_massege = "success"
            self.re_data = self.list_items
        else:
            self.re_status = status.HTTP_404_NOT_FOUND
            self.re_massege = "not found"
            self.re_data = None
        return [self.re_status, self.re_massege, self.re_data, self.page]

    def open_m_category(self):
        try:
            m_category = MainCategoryModel.objects.get(id=self.request.GET.get('id_m_category'))
        except:
            m_category = None
        if m_category:
            try:
                image = m_category.image.url
            except:
                image = ""
            self.re_status = status.HTTP_200_OK
            self.re_massege = "success"
            self.re_data = {
                "id_m_category": m_category.id,
                "name": m_category.name,
                "description": m_category.description,
                "image": image,
                "created_at": m_category.created_at.strftime("%d-%m-%y %H:%M"),
            }
        else:
            self.re_status = status.HTTP_404_NOT_FOUND
            self.re_massege = "Not Found"
            self.re_data = None
        return [self.re_status, self.re_massege, self.re_data]

    def check_inputs(self):
        self.re_status = status.HTTP_400_BAD_REQUEST
        self.re_massege = "bad request"
        if self.name is None or self.name == "":
            self.re_massege = "please enter your name"
        elif len(self.name) <= 5:
            self.re_massege = "the minimum character is 6"
        elif len(self.name) >= 30:
            self.re_massege = "the maximum character is 29"
        elif self.name.isdigit():
            self.re_massege = " please enter characters, not numbers "
        # ----------------------------------------------------------------
        elif self.description is None or self.description == "":
            self.re_massege = "please enter a description"
        elif self.description.isdigit():
            self.re_massege = " please enter characters, not numbers "
        elif len(self.description) <= 5:
            self.re_massege = "the minimum character is 6"
        elif len(self.description) >= 80:
            self.re_massege = "the maximum character is 79"
        elif self.main_exists.exists():
            self.re_massege = "Data already exists"
        elif self.sub_exists.exists():
            self.re_massege = "Data already exists"
        # ------------------------------------------------------------------
        else:
            self.re_status = status.HTTP_100_CONTINUE

    def create_m_category(self):
        self.check_inputs()
        if self.re_status == status.HTTP_100_CONTINUE:
            # existing_categories = MainCategoryModelFilter(data=self.request.POST).qs
            # if existing_categories.exists():
            #     self.re_status = status.HTTP_400_BAD_REQUEST
            #     self.re_massege = "Data already exists"
            #     self.re_data = None
            # else:
            try:
                create = MainCategoryModel.objects.create(
                    name=self.name,
                    description=self.description,
                    image=self.image,
                )
                image_url = create.image.url if create.image else ""
                self.re_status = status.HTTP_201_CREATED
                self.re_massege = "CREATED SUCCESSFUL"
                self.re_data = {
                    "id": create.id,
                    "name": create.name,
                    "description": create.description,
                    "image": image_url,
                }
            except Exception as e:
                self.re_status = status.HTTP_500_INTERNAL_SERVER_ERROR
                self.re_massege = str(e)
                self.re_data = None
        return [self.re_status, self.re_massege, self.re_data]

    def update_m_category(self):
        self.check_inputs()
        if self.re_status == status.HTTP_100_CONTINUE:
            try:
                update_category = self.main_category
                update_category.name = self.name
                update_category.description = self.description
                update_category.image = self.image
                update_category.save()
                image_url = update_category.image.url
                self.re_status = status.HTTP_200_OK
                self.re_massege = "updated"
                self.re_data = {
                    "id_main_category": update_category.id,
                    "name": update_category.name,
                    "description": update_category.description,
                    "image": image_url,
                    "Updated at": update_category.created_at,
                }

            except Exception as e:
                self.re_status = status.HTTP_500_INTERNAL_SERVER_ERROR
                self.re_massege = str(e)
                self.re_data = None
        return [self.re_status, self.re_massege, self.re_data]

    def delete_m_category(self):
        try:
            delete_m_category = MainCategoryModel.objects.get(id=self.request.POST.get("id_m_category"))
            if delete_m_category:
                delete_m_category.delete()
                self.re_status = status.HTTP_200_OK
                self.re_massege = "Deleted"
                self.re_data = None
            else:
                self.re_status = status.HTTP_404_NOT_FOUND
                self.re_massege = "Not Found"
        except Exception as e:
            self.re_status = status.HTTP_500_INTERNAL_SERVER_ERROR
            self.re_massege = str(e)
            self.re_data = None
        return [self.re_status, self.re_massege, self.re_data]

# ----------------------------end class main category---------------------------------


class SubCategoryOop(MainCategory):
    def all_s_category(self):
        sub_category = SubCategory.objects.all()
        if sub_category:
            for category in sub_category:
                try:
                    image = category.image.url
                except:
                    image = None
                category = {
                    "id_main_category": category.main_category.id,
                    "id": category.id,
                    "name": category.name,
                    "image": image,
                }
                self.list_items.append(category)
                self.re_status = status.HTTP_200_OK
                self.re_massege = "success"
                self.re_data = self.list_items
        else:
            self.re_status = status.HTTP_404_NOT_FOUND
            self.re_massege = "Not Found"
            self.re_data = None
        return [self.re_status, self.re_massege, self.re_data]

    def open_s_category(self):
        try:
            get_s_category = SubCategory.objects.get(id=self.request.GET.get('id-sub'))
        except:
            get_s_category = None
        if get_s_category:
            try:
                image, image_main = get_s_category.image.url, get_s_category.main_category.image.url
            except:
                image, image_main = "", ""
            self.re_status = status.HTTP_200_OK
            self.re_massege = "OK"
            self.re_data = {
                "id": get_s_category.id,
                "name": get_s_category.name,
                "description": get_s_category.description,
                "image": image,
                "created_at": get_s_category.created_at.strftime("%d-%m-%y %H:%M"),
                "main category": {
                    "id": get_s_category.main_category.id,
                    "name": get_s_category.main_category.name,
                    "description": get_s_category.main_category.description,
                    "image": image_main,
                    "created_at": get_s_category.main_category.created_at.strftime("%d-%m-%y %H:%M"),
                },

            }
        else:
            self.re_status = status.HTTP_404_NOT_FOUND
            self.re_massege = "NOT FOUND"
            self.re_data = None
        return [self.re_status, self.re_massege, self.re_data]

    def create_s_category(self):
        self.check_inputs()
        if self.re_status == status.HTTP_100_CONTINUE:
            try:
                create = SubCategory.objects.create(
                    main_category=self.main_category,
                    name=self.name,
                    description=self.description,
                    image=self.image,
                )
                image_sub = create.image.url if create.image else ""

                self.re_status = status.HTTP_201_CREATED
                self.re_massege = "created"
                self.re_data = {
                    "id_category": create.id,
                    "name": create.name,
                    "description": create.description,
                    "image": image_sub,
                    "main_category": {
                        "id_main": create.main_category.id,
                        "name": create.main_category.name,

                    }
                }
            except Exception as e:
                self.re_status = status.HTTP_500_INTERNAL_SERVER_ERROR
                self.re_massege = str(e)
                self.re_data = None
        return [self.re_status, self.re_massege, self.re_data]

    def update_s_category(self):
        self.check_inputs()
        if self.re_status == status.HTTP_100_CONTINUE:
            try:
                update = self.sub_category
                update.main_category = self.main_category
                update.name = self.name
                update.description = self.description
                update.image = self.image
                update.save()
                image_url = update.image.url
                self.re_status = status.HTTP_200_OK
                self.re_massege = "updated"
                self.re_data = {
                    "id": update.id,
                    "name": update.name,
                    "description": update.description,
                    "image": image_url,
                    "info_main": {
                        "id-main": update.main_category.id,
                        "name": update.main_category.name,
                    }
                }
            except Exception as e:
                self.re_status = status.HTTP_500_INTERNAL_SERVER_ERROR
                self.re_massege = str(e)
                self.re_data = None
        else:
            self.re_status = status.HTTP_404_NOT_FOUND
            self.re_massege = "NOT FOUND"
        return [self.re_status, self.re_massege, self.re_data]

    def delete_s_category(self):
        try:
            delete = self.sub_category
            if delete:
                delete.delete()
                self.re_status = status.HTTP_200_OK
                self.re_massege = "deleted"
            else:
                self.re_status = status.HTTP_404_NOT_FOUND
                self.re_massege = "not found"
        except Exception as e:
            self.re_status = status.HTTP_500_INTERNAL_SERVER_ERROR
            self.re_massege = str(e)
        return [self.re_status, self.re_massege]

>>>>>>> 8ef536d (create request's category and brand)
