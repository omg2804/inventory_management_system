import pytest
from src.models.product import Product
from src.services.inventory_service import InventoryService

@pytest.fixture
def inventory_service():
    return InventoryService(products=[])


def test_acceptance_add_product(inventory_service):
    product = Product.create(name='New Product', quantity=15, threshold=5)
    inventory_service.add_product(product)
    assert len(inventory_service.products) == 1
    assert inventory_service.products[0].name == 'New Product'


def test_acceptance_update_product_quantity(inventory_service):
    product = Product.create(name='Update Product', quantity=10, threshold=5)
    inventory_service.add_product(product)
    inventory_service.update_product_quantity(product.id, 25)
    assert inventory_service.products[0].quantity == 25


def test_acceptance_remove_product(inventory_service):
    product = Product.create(name='Remove Product', quantity=10, threshold=5)
    inventory_service.add_product(product)
    assert inventory_service.remove_product(product.id) is True
    assert len(inventory_service.products) == 0


def test_acceptance_check_stock(inventory_service):
    product = Product.create(name='Check Stock Product', quantity=10, threshold=5)
    inventory_service.add_product(product)
    assert inventory_service.check_low_stock() == []
    inventory_service.update_product_quantity(product.id, 2)
    low_stock_products = inventory_service.check_low_stock()
    assert len(low_stock_products) == 1
    assert low_stock_products[0].name == 'Check Stock Product'


def test_acceptance_alert_low_stock(inventory_service):
    product1 = Product.create(name='Low Stock Product 1', quantity=3, threshold=5)
    product2 = Product.create(name='Low Stock Product 2', quantity=10, threshold=5)
    inventory_service.add_product(product1)
    inventory_service.add_product(product2)
    low_stock_products = inventory_service.check_low_stock()
    assert len(low_stock_products) == 1
    assert low_stock_products[0].name == 'Low Stock Product 1'


def test_acceptance_end_to_end(inventory_service):
    product = Product.create(name='End-to-End Product', quantity=10, threshold=5)
    inventory_service.add_product(product)
    assert len(inventory_service.products) == 1
    inventory_service.update_product_quantity(product.id, 1)
    low_stock_products = inventory_service.check_low_stock()
    assert len(low_stock_products) == 1
    assert low_stock_products[0].name == 'End-to-End Product'
    assert inventory_service.remove_product(product.id) is True
    assert len(inventory_service.products) == 0