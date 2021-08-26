import json


def _response_maistodos_api():
    return {
        'text': {
            "createdAt": "2021-07-26T22:50:55.740Z",
            "message": "Cashback criado com sucesso!",
            "id": "NaN",
            "document": "23534104056",
            "cashback": "10"
        }
    }


def _create_correct_payload():
    return {
        "sold_at": "2026-01-02 00:00:00",
        "customer": {
            "document": "23534104056",
            "name": "JOSE DA SILVA",
        },
        "total": "10.00",
        "products": [
            {
                "type": "A",
                "value": "10.00",
                "qty": 1,
            }
        ],
    }


def _create_wrong_document_payload():
    payload = _create_correct_payload()
    payload['customer']['document'] = "898"
    return payload


def _create_wrong_total_value_payload():
    payload = _create_correct_payload()
    payload['total'] = "898.00"
    return payload


def _create_wrong_product_type_payload():
    payload = _create_correct_payload()
    payload['products'][0]['type'] = "898"
    return payload


def test_create_cashback(client, mocker):
    data = _create_correct_payload()
    mais_todos_response = _response_maistodos_api()

    mocker.patch('src.services.maistodos_service', mais_todos_response)

    response = client.post("/api/cashback", json.dumps(data))
    assert response.status_code == 201


def test_create_cashback_wrong_document(client, mocker):
    data = _create_wrong_document_payload()
    mais_todos_response = _response_maistodos_api()

    mocker.patch('src.services.maistodos_service', mais_todos_response)

    response = client.post("/api/cashback", json.dumps(data))
    assert response.status_code == 400
    assert response \
        .json()['detail'] == 'Error: [cashback|controller] [cashback|service] Verify the given data. Some of them are invalid'


def test_create_cashback_wrong_total_value(client, mocker):
    data = _create_wrong_total_value_payload()
    mais_todos_response = _response_maistodos_api()

    mocker.patch('src.services.maistodos_service', mais_todos_response)

    response = client.post("/api/cashback", json.dumps(data))
    assert response.status_code == 400
    assert response.json()['detail'] == 'Error: [cashback|controller] [cashback|service] Invalid total value'


def test_create_cashback_wrong_product_type(client, mocker):
    data = _create_wrong_product_type_payload()
    mais_todos_response = _response_maistodos_api()

    mocker.patch('src.services.maistodos_service', mais_todos_response)

    response = client.post("/api/cashback", json.dumps(data))
    assert response.status_code == 400
    assert response.json()['detail'] == 'Error: [cashback|controller] [cashback|service] Invalid product type'
