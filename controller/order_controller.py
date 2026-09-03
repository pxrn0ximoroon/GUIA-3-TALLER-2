"""El controlador, que coordina el modelo con la vista."""

from model.order import Order
from model.payment import PaymentMethod
from model.report import ReportGenerator
from model.repository import OrderRepository
from view.console_view import ConsoleView


class OrderController:
    """Organiza el flujo: pide los cálculos al modelo y los muestra con la vista."""

    def __init__(
        self,
        view: ConsoleView,
        payment: PaymentMethod,
        repository: OrderRepository,
        report: ReportGenerator,
    ):
        """Arma el controlador con la vista, el pago, el guardado y el reporte."""
        self.view = view
        self.payment = payment
        self.repository = repository
        self.report = report

    def run(self, order: Order, order_id: str) -> None:
        """Corre todo el flujo sobre un pedido."""
        total = order.calculate_total()
        self.view.show_total(total)

        self.view.show_message(self.payment.pay(total))
        self.view.show_message(self.repository.save(order_id, total))
        self.view.show_report(self.report.generate(order))
