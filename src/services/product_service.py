import string

from sqlalchemy.orm import Session

from src.dtos.requests.cashback_request import CashbackCreatePayload
from src.dtos.requests.product_request import Product
from src.repository import products_repository


def _sanitize_product(product: Product) -> dict:
    return {
        'type': product.type,
        'value': float(product.value),
        'qty': product.qty
    }


def _create_product(product: Product, database: Session):
    sanitized_product = _sanitize_product(product)
    return products_repository.create_product(sanitized_product, database)


def save_products(cashback_payload: CashbackCreatePayload, database: Session):
    try:
        map(lambda product: _create_product(product, database), cashback_payload.products)
    except BaseException:
        raise Exception('Error on create product(s)')


def validate_product_type(products):
    try:
        valid_types = set(string.ascii_uppercase)
        product_types = set(map(lambda product: product.type, products))
        differences = product_types.difference(valid_types)

        if differences:
            raise
    except BaseException:
        raise Exception('Invalid product type')
