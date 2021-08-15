import json

import requests

from src.core.settings import settings


def _create_payload_data(customer_document, cashback_value):
    return {
        'document': customer_document,
        'cashback': str(cashback_value)
    }


def call_maistodos_api(customer_document, cashback_value):
    payload_data = _create_payload_data(customer_document, cashback_value)
    return requests.post(settings.MAISTODOS_URL, json.dumps(payload_data))
