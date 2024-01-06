from ...models import *
# from ....settings.models import *
from rest_framework import status


class ProductOops:
    def __init__(self, request):
        self.request = request
        self.list_items = []
        self.re_status, self.re_massege, self.re_data = status.HTTP_404_NOT_FOUND, "", None
        try:
            self.name = self.request.POST.get('name')
        except:
            self.name = None
        try:
            self.category = Category.objects.get(
                id=self.request.POST.get('id_category', self.request.GET.get('id_category')))

        except:
            self.category = None
        # try:
        #     self.brand = Brand.objects.get(id=self.request.GET.get('id_brand'))
        # except:
        #     self.brand = None
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

    def all(self):
        get_products = Product.objects.all()
        if get_products:
            for product in get_products:
                product = {
                    "id_product": product.id,
                    "name": product.name,
                    "category": product.id,
                    # "brand": product.brand,
                    "description": product.description,
                    "price": product.price,
                    "cost": product.cost,
                    "created_at": product.created_at,
                }
                self.list_items.append(product)
            self.re_status = status.HTTP_200_OK
            self.re_massege = "success"
            self.re_data = self.list_items
        else:
            self.re_status = status.HTTP_404_NOT_FOUND
            self.re_massege = "NOT FOUND"
            self.re_data = None
        return [self.re_status, self.re_massege, self.re_data]
