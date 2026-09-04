"""Los métodos de pago."""

from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    """Modelo base para cualquier método de pago."""

    @abstractmethod
    def pay(self, amount: float) -> str:
        """Procesa el pago de un monto."""


class CardPayment(PaymentMethod):
    """Pago con tarjeta."""

    def pay(self, amount: float) -> str:
        return f"Procesando pago con tarjeta por {amount:.2f}"


class CashPayment(PaymentMethod):
    """Pago en efectivo."""

    def pay(self, amount: float) -> str:
        return f"Procesando pago en efectivo por {amount:.2f}"


class TransferPayment(PaymentMethod):
    """Pago por transferencia bancaria."""

    def pay(self, amount: float) -> str:
        return f"Procesando transferencia bancaria por {amount:.2f}"
