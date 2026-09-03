"""Arranca el sistema: crea los objetos, los conecta y corre el pedido."""

from controller.order_controller import OrderController
from model.discount import VipDiscount
from model.order import Order
from model.payment import CardPayment
from model.report import TextReport
from model.repository import OrderRepository
from view.console_view import ConsoleView

ITEMS = [10000, 25000, 5000]


def main() -> None:
    """Corre el flujo completo con un pedido de ejemplo."""
    order = Order(ITEMS, VipDiscount())
    view = ConsoleView()
    controller = OrderController(view, CardPayment(), OrderRepository(), TextReport())
    controller.run(order, "ORD-001")


if __name__ == "__main__":
    main()
