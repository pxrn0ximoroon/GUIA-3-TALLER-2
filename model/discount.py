"""Los descuentos que se le aplican a un pedido."""

from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    """Plantilla para los descuentos."""

    @abstractmethod
    def apply(self, subtotal: float) -> float:
        """Aplica el descuento al subtotal."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Nombre del descuento."""


class RegularDiscount(DiscountStrategy):
    """Descuento del 10 % para clientes normales."""

    @property
    def name(self) -> str:
        return "regular"

    def apply(self, subtotal: float) -> float:
        return subtotal * 0.9


class VipDiscount(DiscountStrategy):
    """Descuento del 20 % para clientes VIP."""

    @property
    def name(self) -> str:
        return "vip"

    def apply(self, subtotal: float) -> float:
        return subtotal * 0.8


class EmployeeDiscount(DiscountStrategy):
    """Descuento del 50 % para empleados."""

    @property
    def name(self) -> str:
        return "employee"

    def apply(self, subtotal: float) -> float:
        return subtotal * 0.5


class StudentDiscount(DiscountStrategy):
    """Descuento del 15 % para estudiantes (función nueva)."""

    @property
    def name(self) -> str:
        return "student"

    def apply(self, subtotal: float) -> float:
        return subtotal * 0.85
