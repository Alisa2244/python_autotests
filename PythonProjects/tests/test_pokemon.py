import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'df7280ed44fda2ec7ac2b2f0b3356000'
HEADER = {
    'Content-Type': 'application/json',
    'trainer_token': TOKEN
}
TRAINER_ID='11240'

def test_status_code():
    response_trainers = requests.get(url=f'{URL}/trainers', headers=HEADER)
    assert response_trainers.status_code == 200 # Тест на статус код

def test_trainer_id():
    response_id = requests.get(url=f'{URL}/trainers', params={'trainer_id':TRAINER_ID})
    assert response_id.json()['data'][0]['id']==TRAINER_ID # Тест на проверку наличия моего тренера    