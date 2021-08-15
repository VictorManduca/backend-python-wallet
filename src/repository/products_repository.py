from sqlalchemy.orm import Session

from src.database.models.products_model import Products
from src.dtos.requests.product_request import Product


def create_product(payload: Product, database: Session):
    try:
        product = Products(**payload)

        database.add(product)
        database.commit()
        database.refresh(product)

        return product
    except BaseException as exception:
        raise Exception('[product|repository]  {}'.format(exception))
