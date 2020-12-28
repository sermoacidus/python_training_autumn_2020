from tasks_hw11.task2_hw11 import Order, elder_discount, morning_discount


def test_if_discount_is_working():
    order_1 = Order(100, morning_discount)
    assert order_1.final_price() == 50
    order_2 = Order(100, elder_discount)
    assert order_2.final_price() == 10


def test_if_possible_to_change_discount_in_the_runtime():
    order_2 = Order(100, elder_discount)
    assert order_2.final_price() == 10
    order_2.discount = morning_discount
    assert order_2.final_price() == 50
