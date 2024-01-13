from ...models import *
from settings.models import *
from rest_framework import status
from django.core.paginator import Paginator


class ProductOops:
    def __init__(self, request):
        self.request = request
        self.list_items = []
        self.re_status, self.re_massege, self.re_data = status.HTTP_404_NOT_FOUND, "", None
        self.page_number = self.request.GET.get("page", 1)  # تعيين قيمة افتراضية

        try:
            self.name = self.request.POST.get('name')
        except:
            self.name = None
        try:
            self.category = Category.objects.get(
                id=self.request.POST.get('id_category', self.request.GET.get('id_category')))

        except:
            self.category = None
        try:
            self.brand = Brand.objects.get(id=self.request.GET.get('id_brand'))
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
            self.create_at = self.request.POST.get('create_at')
        except:
            self.create_at = None

    # def all(self):
    #     get_products = Product.objects.all()
    #     paginator = Paginator(get_products, 2)  # Show 2 contacts per page.
    #     page = paginator.get_page(self.page_number)
    #     if get_products:
    #         for product in get_products:
    #             product = {
    #                 "id_product": product.id,
    #                 "name": product.name,
    #                 "category": product.category.name,
    #                 "brand": product.brand.name,
    #                 "description": product.description,
    #                 "price": product.price,
    #                 "cost": product.cost,
    #                 "created_at": product.created_at,
    #
    #             }
    #             self.list_items.append(product)
    #         self.re_status = status.HTTP_200_OK
    #         self.re_massege = "success"
    #         self.re_data = self.list_items
    #     else:
    #         self.re_status = status.HTTP_404_NOT_FOUND
    #         self.re_massege = "NOT FOUND"
    #         self.re_data = None
    #     return [self.re_status, self.re_massege, self.re_data]
    def all(self):
        products = Paginator(Product.objects.all(), 3).get_page(self.page_number)
        if products:
            for product in products:
                product_info = {
                    "id_product": product.id,
                    "name": product.name,
                    "category": product.category.name if product.category else None,
                    "brand": product.brand.name if product.brand else None,
                    "description": product.description,
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

        return [self.re_status, self.re_massege, self.re_data]

    def open(self):
        product = Product.objects.get(id=self.request.GET.get("id_product"))
        if product:
            self.re_status = status.HTTP_200_OK
            self.re_massege = "opened"
            self.re_data = {
                "id_product": product.id,
                "name": product.name,
                "category": product.category.name,
                "brand": product.brand.name,
                "description": product.description,
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
        if self.name is None or self.name == "":
            self.re_massege = "please enter product name"
        elif len(self.name) <= 5:
            self.re_massege = "the minimum character is 6"
        elif len(self.name) >= 15:
            self.re_massege = "the maximum character is 14"
# -------------------------------------------------------------------------
        elif self.description is None or self.description == "":
            self.re_massege = " please enter description"
        elif len(self.description) <= 5:
            self.re_massege = "the minimum character 4"
        elif len(self.description) >= 80:
            self.re_massege = "the maximum character 79"
# --------------------------------------------------------------------------
        elif self.price == 0:
            self.re_massege = "please enter a price"
        elif self.price <= 5:
            self.re_massege = "The minimum price is 6"
        elif self.price >= 50000:
            self.re_massege = "The maximum price is 49999"
# -------------------------------------------------------------------------
        elif self.cost == 0:
            self.re_massege = "please enter a cost"
        elif self.cost <= 4:
            self.re_massege = "The minimum cost is 3"
        elif self.cost >= 40000:
            self.re_massege = "The maximum cost is 39999"
# ---------------------------------------------------------------------------
        else:
            self.re_status = status.HTTP_100_CONTINUE
        return [self.re_status, self.re_massege, self.re_data]
