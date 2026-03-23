from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID, uuid4

@dataclass
class Product:
    id: UUID
    name: str
    quantity: int
    threshold: int

    @classmethod
    def create(cls, name: str, quantity: int, threshold: int) -> Product:
        return cls(id=uuid4(), name=name, quantity=quantity, threshold=threshold)