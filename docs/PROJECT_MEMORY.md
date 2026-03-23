# Project Memory

## Original Request
create an inventory management system in python that tracks products, quantities and can alert when stock is low.

## Architecture Blueprint
{'project_name': 'Inventory Management System', 'files': [{'path': 'src/models/product.py', 'purpose': 'Defines the Product model for tracking inventory items.', 'exports': ['Product'], 'imports_from': [], 'third_party_deps': [], 'model_schema': {'Product': {'fields': {'id': 'UUID', 'name': 'str', 'quantity': 'int', 'threshold': 'int'}}}, 'fields': {}}, {'path': 'src/services/inventory_service.py', 'purpose': 'Contains business logic for managing inventory.', 'exports': ['InventoryService'], 'imports_from': ['src/models/product.py'], 'third_party_deps': [], 'model_schema': {'InventoryService': {'fields': {'products': 'list[Product]'}}}, 'fields': {}}, {'path': 'src/interface/cli.py', 'purpose': 'Handles user interaction through command line interface.', 'exports': ['main'], 'imports_from': ['src/services/inventory_service.py'], 'third_party_deps': [], 'model_schema': {}, 'fields': {}}], 'dependency_order': ['src/models/', 'src/services/', 'src/interface/'], 'third_party_packages': []}

## Coding Rules
- Follow modular boundaries.
- Internal imports must be absolute (`src.*`).
- Keep type annotations and docstrings in generated code.
