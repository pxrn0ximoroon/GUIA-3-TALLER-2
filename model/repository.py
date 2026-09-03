"""El guardado del pedido."""


class OrderRepository:
    """Guarda el pedido (MySQL, por ahora)."""

    def save(self, order_id: str, total: float) -> str:
        """Guarda el pedido y devuelve un mensaje."""
        return f"Guardando pedido {order_id} por {total:.2f} en MySQL..."
