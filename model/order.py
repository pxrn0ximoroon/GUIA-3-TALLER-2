"""El modelo del pedido."""

from model.discount import DiscountStrategy


class Order:
    """Un pedido; se encarga solo de los cálculos (suma, descuento e impuesto)."""

    TAX_RATE = 0.19

    def __init__(self, items: list[float], discount: DiscountStrategy):
        """Arma un pedido con los productos y el descuento."""
        self.items = list(items)
        self.discount = discount

    def raw_total(self) -> float:
        """Suma los productos sin descuento ni impuesto."""
        return sum(self.items)

    def discount_total(self) -> float:
        """El subtotal después de aplicar el descuento."""
        return self.discount.apply(self.raw_total())

    def tax_amount(self) -> float:
        """El valor del impuesto (IVA del 19 %)."""
        return self.discount_total() * self.TAX_RATE

    def calculate_total(self) -> float:
        """El total final a pagar (descuento + impuesto)."""
        return self.discount_total() * (1 + self.TAX_RATE)
