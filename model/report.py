"""Los reportes del pedido."""

from abc import ABC, abstractmethod

from model.order import Order


class ReportGenerator(ABC):
    """Modelo base para generar reportes."""

    @abstractmethod
    def generate(self, order: Order) -> str:
        """Genera la versión del pedido en ese formato."""


class TextReport(ReportGenerator):
    """Reporte en texto plano."""

    def generate(self, order: Order) -> str:
        return f"Pedido con total {order.calculate_total():.2f}"


class CsvReport(ReportGenerator):
    """Reporte en formato CSV."""

    def generate(self, order: Order) -> str:
        return f"total,{order.calculate_total():.2f}"


class JsonReport(ReportGenerator):
    """Reporte en formato JSON."""

    def generate(self, order: Order) -> str:
        return f'{{"total": {order.calculate_total():.2f}}}'
