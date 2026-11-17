import json
from pathlib import Path

import pytest
import yaml


@pytest.mark.parametrize('item', json.loads(
    (Path(__file__).parents[1] / 'examples/guest_links.json').read_text('utf-8')
))
def test_guest_documents_round_trip(client, item):
    created = client.post('/api/id/', json=item)
    assert created.status_code == 201
    resolved = client.get(f'/api/id/{item["custom_id"]}/')
    assert resolved.json == {'url': item['url']}
    redirect = client.get(f'/{item["custom_id"]}')
    assert redirect.status_code == 302
    assert redirect.location == item['url']


def test_guest_home_and_local_assets(client):
    page = client.get('/').get_data(as_text=True)
    assert 'HotelLinks' in page
    assert 'Меню, правила проживания, маршруты и контакты' in page
    assert 'code.jquery.com' not in page
    assert client.get('/static/js/bootstrap.bundle.min.js').status_code == 200
    assert client.get('/static/img/hotellinks.svg').status_code == 200


def test_openapi_guest_examples():
    spec = yaml.safe_load(
        (Path(__file__).parents[1] / 'openapi.yml').read_text('utf-8')
    )
    assert spec['info']['title'].startswith('HotelLinks')
    assert spec['servers'][0]['url'] == 'http://127.0.0.1:8005'
    assert '/api/id/' in spec['paths']
