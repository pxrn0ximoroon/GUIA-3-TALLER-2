class OrderSystem:
    """Sistema inicial de pedidos con múltiples responsabilidades."""

    def __init__(self, customer_type, items, payment_method):
        """Inicializa el sistema con el tipo de cliente, los productos y el método de pago."""
        self.customer_type = customer_type
        self.items = items
        self.payment_method = payment_method

    def calculate_total(self):
        """Calcula el total del pedido aplicando descuento e impuesto."""
        total = sum(self.items)

        if self.customer_type == "regular":
            total *= 0.9
        elif self.customer_type == "vip":
            total *= 0.8
        elif self.customer_type == "employee":
            total *= 0.5

        total *= 1.19
        return total

    def process_payment(self):
        """Procesa el pago según el método seleccionado."""
        if self.payment_method == "card":
            print("Procesando pago con tarjeta")
        elif self.payment_method == "cash":
            print("Procesando pago en efectivo")
        elif self.payment_method == "transfer":
            print("Procesando transferencia bancaria")

    def save_order(self, order_id):
        """Guarda el pedido en una base de datos concreta."""
        print(f"Guardando pedido {order_id} en MySQL...")

    def generate_report(self, format_type):
        """Genera un reporte del pedido en el formato solicitado."""
        total = self.calculate_total()

        if format_type == "text":
            return f"Pedido con total {total}"
        if format_type == "csv":
            return f"total,{total}"
        if format_type == "json":
            return f'{{"total": {total}}}'

        return "Formato no soportado"


def main():
    """Función principal de ejecución del sistema."""

    # Datos de ejemplo
    customer_type = "vip"
    items = [10000, 25000, 5000]
    payment_method = "card"
    report_format = "text"
    order_id = "ORD-001"

    # Crear sistema
    order_system = OrderSystem(customer_type, items, payment_method)

    # Calcular total
    total = order_system.calculate_total()
    print(f"Total calculado: {total}")

    # Procesar pago
    order_system.process_payment()

    # Guardar pedido
    order_system.save_order(order_id)

    # Generar reporte
    report = order_system.generate_report(report_format)
    print("Reporte:")
    print(report)


if __name__ == "__main__":
    main()
