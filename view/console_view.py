"""La vista de consola, donde se imprime todo."""


class ConsoleView:
    """Muestra los mensajes al usuario por consola."""

    def show_total(self, total: float) -> None:
        """Muestra el total calculado."""
        print(f"Total calculado: {total:.2f}")

    def show_report(self, report: str) -> None:
        """Muestra el contenido de un reporte."""
        print("Reporte:")
        print(report)

    def show_message(self, message: str) -> None:
        """Muestra un mensaje cualquiera."""
        print(message)
