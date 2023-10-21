# 使用一等函数实现设计模式
import inspect
from collections.abc import Sequence
from dataclasses import dataclass
from decimal import Decimal
from typing import Optional, Callable, NamedTuple
from chapter9 import closure_learn


class Customer(NamedTuple):
    name: str
    fidelity: int


class LineItem(NamedTuple):
    product: str
    quantity: int
    price: Decimal

    def total(self):
        return self.price * self.quantity


@dataclass(frozen=True)
class Order:
    customer: Customer
    cart: Sequence[LineItem]
    promotion: Optional[Callable[['Order'], Decimal]] = None

    def total(self) -> Decimal:
        totals = (item.total() for item in self.cart)
        return sum(totals, start=Decimal(0))

    def deu(self) -> Decimal:
        if self.promotion is None:
            discount = Decimal(0)
        else:
            discount = self.promotion(self)

        return self.total() - discount

    def __repr__(self):
        return f'<Order total: {self.total():.2f} due: {self.due():.2f}>'


def fidelity_promo(order: Order) -> Decimal:
    if order.customer.fidelity >= 1000:
        return order.total() * Decimal('0.05')
    return Decimal(0)


def bulk_item_promo(order: Order) -> Decimal:
    discount = Decimal(0)
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * Decimal('0.1')
    return discount


def large_order_promo(order: Order) -> Decimal:
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * Decimal('0.07')
    return Decimal(0)


# 选择最佳策略的简单方式
promos = [fidelity_promo, bulk_item_promo, large_order_promo, ]


def best_promo(order: Order) -> Decimal:
    # 可以通过模块内省的机制实现, 但是潜在的隐性要求是 模块中只能包含对应的函数.
    [print(func) for _, func in inspect.getmembers(closure_learn, inspect.isfunction)]
    """
        选择可用的最佳折扣
    :param order:  订单
    :return: 折扣
    """
    return max(promo(order) for promo in promos)


# 使用装饰器改进策略模式
Promotion = Callable[[Order], Decimal]

promos2: list[Promotion] = []


def promotion(promo: Promotion) -> Promotion:
    promos.append(promo)
    return promo


@promotion
def fidelity_promo2(order: Order) -> Decimal:
    if order.customer.fidelity >= 1000:
        return order.total() * Decimal('0.05')
    return Decimal(0)


@promotion
def bulk_item_promo2(order: Order) -> Decimal:
    discount = Decimal(0)
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * Decimal('0.1')
    return discount


@promotion
def large_order_promo2(order: Order) -> Decimal:
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * Decimal('0.07')
    return Decimal(0)


def best_promo2(order: Order) -> Decimal:
    """
        选择可用的最佳折扣
    :param order:  订单
    :return: 折扣
    """
    return max(promo(order) for promo in promos2)


if __name__ == '__main__':
    [print(name) for name, _ in globals().items()]
