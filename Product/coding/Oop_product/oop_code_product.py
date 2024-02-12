from ...models import *
from settings.models import *
from rest_framework import status
from django.core.paginator import Paginator


class ProductOops:
    def __init__(self, request):
        self.request = request
        self.list_items = []
        self.re_status, self.re_massege, self.re_data = status.HTTP_404_NOT_FOUND, "", None
        self.page = self.request.GET.get("page", 1)  # تعيين قيمة افتراضية
        self.product_exists = ProductFilter(data=self.request.POST).qs
        try:
            self.product = Product.objects.get(id=self.request.POST.get('id_product'))
        except:
            self.product = None
        try:
            self.name = self.request.POST.get('name')
        except:
            self.name = None
        try:
            self.main_category = MainCategoryModel.objects.get(id=self.request.POST.get('id_main'))
        except:
            self.main_category = None
        try:
            self.sub_category = SubCategory.objects.get(id=self.request.POST.get('id_sub', self.request.GET.get('id_sub')))
        except:
            self.sub_category = None
        try:
            self.brand = Brand.objects.get(id=self.request.POST.get('id_brand', self.request.GET.get('id_brand')))
        except:
            self.brand = None
        try:
            self.description = self.request.POST.get('description')
        except:
            self.description = None
        try:
            self.price = float(self.request.POST.get('price'))
        except:
            self.price = 0
        try:
            self.cost = float(self.request.POST.get('cost'))
        except:
            self.cost = 0
        try:
            self.image = self.request.FILES.get('image', None)
        except:
            self.image = None

    def all(self):
        products = Paginator(Product.objects.all(), 20).get_page(self.page)
        if products:

            for product in products:
                try:  # that's if product created without image Don't get 500 error
                    image_url = product.image.url
                except:
                    image_url = None
                product_info = {
                    "id_product": product.id,
                    "name": product.name,
                    "category": product.category.name if product.category else None,
                    "brand": product.brand.name if product.brand else None,
                    "description": product.description,
                    "image": image_url,
                    "price": product.price,
                    "cost": product.cost,
                    "created_at": product.created_at,
                }
                self.list_items.append(product_info)
            self.re_status = status.HTTP_200_OK
            self.re_massege = "success"
            self.re_data = self.list_items
        else:
            self.re_status = status.HTTP_404_NOT_FOUND
            self.re_massege = "NOT FOUND"
            self.re_data = None

        return [self.re_status, self.re_massege, self.re_data, self.page]

    def open(self):
        try:
            product = Product.objects.get(id=self.request.GET.get("id_product"))
        except:
            product = None
        if product:
            try:  # that's if product created without image Don't get 500 error
                image_url = product.image.url
            except:
                image_url = None
            self.re_status = status.HTTP_200_OK
            self.re_massege = "opened"
            self.re_data = {
                "id_product": product.id,
                "name": product.name,
                "category": product.category.name,
                "brand": product.brand.name,
                "description": product.description,
                "image": image_url,
                "price": product.price,
                "cost": product.cost,
                "created_at": product.created_at,
            }
        else:
            self.re_status = status.HTTP_404_NOT_FOUND
            self.re_massege = "Not Found"
            self.re_data = None
        return [self.re_status, self.re_massege, self.re_data]

    def check_input(self):
        self.re_status = status.HTTP_400_BAD_REQUEST
        self.re_massege = " Bad Request"
        # if self.product_exists.exists:
        #     self.re_massege = " The Data is already Existed" there is bug here he get only data
# --------------------------------------------------------------------------------
        if Product.objects.filter(name=self.name).exists():
            self.re_massege = "The Name already existed"
        elif self.name is None or self.name == "":
            self.re_massege = "please enter product name"
        elif len(self.name) <= 5:
            self.re_massege = "the minimum character is 6"
        elif len(self.name) >= 30:
            self.re_massege = "the maximum character is 29"
# -------------------------name----------------------------------------------------
        elif self.description is None or self.description == "":
            self.re_massege = " please enter description"
        elif len(self.description) <= 5:
            self.re_massege = "the minimum character 4"
        elif len(self.description) >= 80:
            self.re_massege = "the maximum character 79"
# --------------------------description---------------------------------------------
        elif self.price == 0:
            self.re_massege = "please enter a price"
        elif self.price <= 5:
            self.re_massege = "The minimum price is 6"
        elif self.price >= 90000:
            self.re_massege = "The maximum price is 59999"
# --------------------------price--------------------------------------
        elif self.cost == 0:
            self.re_massege = "please enter a cost"
        elif self.cost <= 4:
            self.re_massege = "The minimum cost is 3"
        elif self.cost >= 80000:
            self.re_massege = "The maximum cost is 79999"
# --------------------------cost-------------------------------------------
        else:
            self.re_status = status.HTTP_100_CONTINUE
            self.re_massege = " CONTINUE"

    def create_product(self):
        self.check_input()
        if self.re_status == status.HTTP_100_CONTINUE:
            try:
                create_product = Product.objects.create(
                    name=self.name,
                    brand=self.brand,
                    description=self.description,
                    price=self.price,
                    cost=self.cost,
                    image=self.image,
                    category=self.sub_category
                )
                self.re_status = status.HTTP_201_CREATED
                self.re_massege = "created"
                self.re_data = {
                    "id_product": create_product.id,
                    "name": create_product.name,
                    "id_category": create_product.category.name if self.sub_category else None,
                    "id_brand": create_product.brand.name if self.brand else None,
                    "description": create_product.description,
                    "image": create_product.image.url,
                    "price": create_product.price,
                    "cost": create_product.cost,
                    "created": create_product.created_at,
                }
            except Exception as e:
                self.re_status = status.HTTP_500_INTERNAL_SERVER_ERROR
                self.re_massege = str(e)
                self.re_data = None

        return [self.re_status, self.re_massege, self.re_data]

    def update_product(self):
        try:
            update_pro = Product.objects.get(id=self.request.POST.get("id_product"))
        except:
            update_pro = None
        if update_pro:
            update_pro.name = self.name
            update_pro.description = self.description
            update_pro.category = self.sub_category
            update_pro.brand = self.brand
            update_pro.price = self.price
            update_pro.cost = self.cost
            update_pro.save()
            self.re_status = status.HTTP_200_OK
            self.re_massege = "updated"
            self.re_data = {
                "id_product": update_pro.id,
                "name": update_pro.name,
                "category": update_pro.category.name,
                "brand": update_pro.brand.name,
                "description": update_pro.description,
                "price": update_pro.price,
                "cost": update_pro.cost,
            }
        else:
            self.re_status = status.HTTP_404_NOT_FOUND
            self.re_massege = "Not Found"
            self.re_data = None
        return [self.re_status, self.re_massege, self.re_data]

    def delete(self):
        delete = self.product
        if delete:
            delete.delete()
            self.re_status = status.HTTP_200_OK
            self.re_massege = "DELETED"
        else:
            self.re_status = status.HTTP_404_NOT_FOUND
            self.re_massege = "NOT FOUND"
        return [self.re_status, self.re_massege]


