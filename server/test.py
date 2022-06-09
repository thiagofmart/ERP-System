import requests

server = 'http://127.0.0.1:8000'

def test_create_enterprise():
    payload = {
        "id": "06.330.557/0001-77",
        "formal_name": "SOLAR AR CONDICIONADO LTDA.",
        "informal_name": "SOLAR AR CONDICIONADO",
        "address": "Av. Antonio Munhoz Bonilha",
        "number": "543",
        "complement": "545",
        "district": "Vila Palmeiras",
        "city": "São Paulo",
        "county": "SP",
        "postal_code": "02.725-055",
        "country": "Brazil",
        "phone": "+55 (11) 3951-5407",
        "site": "www.solarar.com.br",
        "main_email": "solar@solarar.com.br",
        "purchase_email": {
            "email": "compras@solarar.com.br",
            "password": "Solar@2022",
            "assign": ""
        },
        "bill_receiver_email": "solar.nf@solarar.com.br",
        "bill_sender_email": {
            "email": "faturamento@solarar.com.br",
            "password": "Sol@r0201#2020",
            "assign": ""
        },
       "financial_email": {
        "email": "financeiro@solarar.com.br",
        "password": "Sol@rFin#2020",
        "assign": ""
        },
        "additional_content":{
                'regime_tributario':'lucro real',
                'ie':'116.849.891.114',
                'im':'3.333.176-6',
            },
        "logo": "data:image/jpeg;base64"+"base64img",
    }
    response = requests.post(server+'/api/v1/enterprise/create', json=payload)
    return response

def test_create_accredited_person():
    payload = {
        "id": "06.330.557/0001-77",
        "informal_name": "SOLAR AR CONDICIONADO LTDA.",
        "formal_name": "SOLAR AR CONDICIONADO",
        "address": "Av. Antonio Munhoz Bonilha",
        "number": "543",
        "complement": "545",
        "district": "Vila Palmeiras",
        "city": "São Paulo",
        "county": "SP",
        "postal_code": "02.725-055",
        "country": "Brazil",
        "phone": "+55 (11) 3951-5407",
        "site": "www.solarar.com.br",
        "main_email": "solar@solarar.com.br",
        "budget_email_receivers": "thiago.martins@solarar.com.br",
        "purchase_request_email_receivers": "thiago.martins@solarar.com.br",
        "bill_email_receivers": "thiago.martins@solarar.com.br",
        "additional_content": {
                'regime_tributario':'lucro real',
                'ie':'116.849.891.114',
                'im':'3.333.176-6',
            }
        }
    response = requests.post(
        server+"/api/v1/accredited_person/create",
        json=payload
        )
    return response
def test_create_budget():
    pass
def test_purchase_request():
    payload = {
    "requester": "Thiago",
    "budget_id": 1,
    "provider_id": 1,
    "items": [
        {
        "descricao": "COMPRESSOR",
        "qtd": 1,
        "unidade": "UN",
        "unitario": 10,
        "total": 10
        }
    ],
    "payment_terms": "30 DDL"
    }
    requests.post(server+'', data={})
