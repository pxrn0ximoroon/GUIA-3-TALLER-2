"""Pruebas de pago, guardado y reportes."""

from model.discount import VipDiscount
from model.order import Order
from model.payment import CardPayment, CashPayment, PaymentMethod, TransferPayment
from model.report import CsvReport, JsonReport, TextReport
from model.repository import OrderRepository


def make_order():
    return Order([10000, 25000, 5000], VipDiscount())


def test_payment_methods_produce_message():
    order = make_order()
    amount = order.calculate_total()
    for method in (CardPayment(), CashPayment(), TransferPayment()):
        message = method.pay(amount)
        assert isinstance(message, str)
        assert len(message) > 0


def test_all_payment_methods_share_the_abstraction():
    order = make_order()
    amount = order.calculate_total()
    methods = [CardPayment(), CashPayment(), TransferPayment()]
    for method in methods:
        assert isinstance(method, PaymentMethod)
        assert "Procesando" in method.pay(amount)


def test_repository_saves_order_with_id_and_total():
    repository = OrderRepository()
    message = repository.save("ORD-001", 38080)
    assert "ORD-001" in message
    assert "38080" in message


def test_text_report_generator():
    report = TextReport().generate(make_order())
    assert report.startswith("Pedido con total")


def test_csv_report_generator():
    report = CsvReport().generate(make_order())
    assert report.startswith("total,")


def test_json_report_generator():
    report = JsonReport().generate(make_order())
    assert report == '{"total": 38080.00}'
