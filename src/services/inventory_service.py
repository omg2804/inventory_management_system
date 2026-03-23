from src.models.product import Product

class InventoryService:
    def __init__(self, products: list[Product]):
        self.products = products

    def add_product(self, product: Product) -> None:
        if product is None:
            raise ValueError("Product cannot be None")
        self.products.append(product)

    def remove_product(self, product_id: str) -> bool:
        if not product_id:
            raise ValueError("Product ID cannot be empty or None")
        for product in self.products:
            if product.id == product_id:
                self.products.remove(product)
                return True
        return False

    def update_product_quantity(self, product_id: str, quantity: int) -> bool:
        if not product_id:
            raise ValueError("Product ID cannot be empty or None")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        for product in self.products:
            if product.id == product_id:
                product.quantity = quantity
                return True
        return False

    def check_low_stock(self) -> list[Product]:
        low_stock_products = [product for product in self.products if product.quantity < product.threshold]
        return low_stock_products