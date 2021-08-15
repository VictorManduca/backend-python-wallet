import json
from datetime import datetime

from cpf_generator import CPF
from sqlalchemy.orm import Session

from src.database.models.api_request_model import Api_Request
from src.database.models.api_response_model import Api_Response
from src.dtos.requests.cashback_request import CashbackCreatePayload
from src.repository import cashback_repository
from src.services import maistodos_service
from src.services import product_service


def _define_cashback_percentage(percentage):
    return percentage


def _generate_cashback(percentage, total_value):
    return float((percentage / 100) * total_value)


def _sanitize_cashback(cashback: CashbackCreatePayload) -> dict:
    try:
        if not CPF.validate(cashback.customer.document):
            raise

        sold_at = datetime.strptime(cashback.sold_at, '%Y-%m-%d %H:%M:%S')
        total_value = float(cashback.total)

        return {
            'sold_at': sold_at,
            'customer_document': cashback.customer.document,
            'customer_name': cashback.customer.name,
            'total_value': total_value
        }
    except BaseException:
        raise Exception('Verify the given data. Some of them are invalid')


def _save_cashback_request(api_request: Api_Request, database: Session):
    return cashback_repository.create_api_request(api_request, database)


def _get_total_sum(products):
    try:
        total_sum = 0
        for product in products:
            total_sum += float(float(product.value) * int(product.qty))

        return total_sum
    except BaseException:
        raise Exception("Invalid product's value or quantity")


def _validate_total_sum(products, given_total_value):
    try:
        total_sum = _get_total_sum(products)
        if not total_sum == given_total_value:
            raise
    except BaseException:
        raise Exception('Invalid total value')


def _validate_given_data(cashback_payload: CashbackCreatePayload):
    product_service.validate_product_type(cashback_payload.products)
    _validate_total_sum(cashback_payload.products, float(cashback_payload.total))


def _build_dictionary_api_response(document, total_value):
    try:
        defined_cashback_value = _define_cashback_percentage(15)
        generated_cashback = _generate_cashback(defined_cashback_value, total_value)
        api_response = maistodos_service.call_maistodos_api(document, generated_cashback)
        json_api_response = json.loads(api_response.text)

        return {
            'createdAt': datetime.strptime(json_api_response['createdAt'], '%Y-%m-%dT%H:%M:%S.%fZ'),
            'cashback_id': json_api_response['id'],
            'document': document,
            'cashback': generated_cashback
        }
    except BaseException:
        raise Exception('Error on call MaisTodos API')


def _save_api_response(document, total_value, database):
    api_response: Api_Response = _build_dictionary_api_response(document, total_value)
    return cashback_repository.create_cashback_response(api_response, database)


def calculate_cashback(cashback_payload: CashbackCreatePayload, database: Session):
    try:
        sanitized_cashback = _sanitize_cashback(cashback_payload)

        _validate_given_data(cashback_payload)
        _save_cashback_request(sanitized_cashback, database)
        product_service.save_products(cashback_payload, database)

        return _save_api_response(sanitized_cashback['customer_document'], sanitized_cashback['total_value'], database)
    except BaseException as exception:
        raise Exception('[cashback|service] {}'.format(exception))
