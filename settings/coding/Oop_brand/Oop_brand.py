from ...models import *
from rest_framework import status
from django.core.paginator import Paginator


class BrandOop:
    def __init__(self, request):
        self.request = request
        self.list_items = []
        self.re_status, self.re_massege, self.re_data = status.HTTP_404_NOT_FOUND, "", None
        self.page = self.request.GET.get("page", 1)
        try:
            self.name = self.request.POST.get("name")
        except:
            self.name = None
        try:
            self.description = self.request.POST.get("description")
        except:
            self.description = None
        try:
            self.brand = Brand.objects.get(id=self.request.POST.get("id_brand"))
        except:
            self.brand = None

    def all(self):
        all_barnd = Paginator(Brand.objects.all(), 20).get_page(self.page)
        if all_barnd:
            for brand in all_barnd:
                brand = {
                    "id": brand.id,
                    "name": brand.name,
                }
                self.list_items.append(brand)
                self.re_status = status.HTTP_200_OK
                self.re_massege = "success"
                self.re_data = self.list_items
        else:
            self.re_status = status.HTTP_404_NOT_FOUND
            self.re_massege = "Not Found"
            self.re_data = None
        return [self.re_status, self.re_massege, self.re_data, self.page]

    def open(self):
        try:
            brand = Brand.objects.get(id=self.request.GET.get('id_brand'))
        except:
            brand = None
        if brand:
            self.re_status = status.HTTP_200_OK
            self.re_massege = "success"
            self.re_data = {
                "id": brand.id,
                "name": brand.name,
                "description": brand.description,
            }
        else:
            self.re_status = status.HTTP_404_NOT_FOUND
            self.re_massege = "NOT FOUND"
            self.re_data = None
        return [self.re_status, self.re_massege, self.re_data]

    def create(self):
        try:
            create = Brand.objects.create(
                name=self.name,
                description=self.description,
            )
            self.re_status = status.HTTP_201_CREATED
            self.re_massege = "created successfully"
            self.re_data = {
                "id": create.id,
                "name": create.name,
                "description": create.description,
            }
        except Exception as e:
            self.re_status = status.HTTP_500_INTERNAL_SERVER_ERROR
            self.re_massege = str(e)
            self.re_data = None
        return [self.re_status, self.re_massege, self.re_data]

    def delete(self):
        try:
            delete = self.brand
        except:
            delete = None
        if delete:
            delete.delete()
            self.re_status = status.HTTP_200_OK
            self.re_massege = "DELETED"
        else:
            self.re_status = status.HTTP_404_NOT_FOUND
            self.re_massege = "NOT FOUND"
        return [self.re_status, self.re_massege]