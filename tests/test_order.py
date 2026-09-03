"""Pruebas del cálculo del pedido y sus descuentos."""

from model.discount import (
    EmployeeDiscount,
    RegularDiscount,
    StudentDiscount,
    VipDiscount,
)
from model.order import Order


def make_order(discount):
    return Order([10000, 25000, 5000], discount)


def test_raw_total_sum_of_products():
    order = make_order(VipDiscount())
    assert order.raw_total() == 40000


def test_vip_order_total_is_expected_reference_value():
    order = make_order(VipDiscount())
    assert order.calculate_total() == 38080


def test_regular_discount_applies_ten_percent():
    order = make_order(RegularDiscount())
    assert order.discount_total() == 36000


def test_employee_discount_is_half_price():
    order = make_order(EmployeeDiscount())
    assert order.discount_total() == 20000


def test_student_discount_new_feature():
    order = make_order(StudentDiscount())
    assert order.discount_total() == 34000


def test_standard_tax_rate_is_nineteen_percent():
    order = make_order(VipDiscount())
    assert order.tax_amount() == 6080


def test_all_discounts_keep_total_positive_when_taxed():
    for discount in (
        RegularDiscount(),
        VipDiscount(),
        EmployeeDiscount(),
        StudentDiscount(),
    ):
        total = make_order(discount).calculate_total()
        assert total > 0
