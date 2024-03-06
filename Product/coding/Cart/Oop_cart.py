from Product.coding.Oop_product.oop_code_product import *


class AddCart(ProductOops):

    def add_to_cart(self):
        add_cart = Cart.objects.create(product=self.product)
        new_variants = self.product.variant.filter(id=self.variant)
        if new_variants.exists():
            for new_variant in new_variants:
                selected_variant = {
                    "id_variant": new_variant.id,
                    "color": new_variant.color.name,
                    "size": new_variant.size.name,
                    "quantity": new_variant.quantity,
                    "price": new_variant.price,
                }
                self.list_items.append(selected_variant)
            self.re_status = status.HTTP_201_CREATED
            self.re_message = "created successfully"
            self.re_data = {
                "id": add_cart.id,
                "product": add_cart.product.id,
                "name": add_cart.product.name,
                "variant": self.list_items
            }
        else:
            self.re_status = status.HTTP_400_BAD_REQUEST
            self.re_message = "bad request"
            self.re_data = None
        return [self.re_status, self.re_message, self.re_data]
