from src.services.inventory_service import InventoryService
from src.models.product import Product

def main():
    products = []
    inventory_service = InventoryService(products)

    while True:
        action = input("Choose an action: add, remove, update, check, exit: ").strip().lower()
        
        if action == "add":
            name = input("Enter product name: ").strip()
            quantity = int(input("Enter product quantity: ").strip())
            threshold = int(input("Enter low stock threshold: ").strip())
            product = Product.create(name, quantity, threshold)
            inventory_service.add_product(product)
            print(f"Added product: {product}")

        elif action == "remove":
            product_id = input("Enter product ID to remove: ").strip()
            inventory_service.remove_product(product_id)
            print(f"Removed product with ID: {product_id}")

        elif action == "update":
            product_id = input("Enter product ID to update: ").strip()
            quantity = int(input("Enter new quantity: ").strip())
            inventory_service.update_product_quantity(product_id, quantity)
            print(f"Updated product ID {product_id} to new quantity: {quantity}")

        elif action == "check":
            low_stock_products = inventory_service.check_low_stock()
            print("Low stock products:", low_stock_products)

        elif action == "exit":
            print("Exiting the inventory management system.")
            break

        else:
            print("Invalid action. Please choose again.")