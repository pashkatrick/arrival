
from http import client
import pytest
from clients.restclient import RestClient

client = RestClient()


@pytest.fixture
def broke_battery():
    payload = {'Voltage': -1}
    # set battery in error mode
    client.post('/api/pins/5/update_pin', data=payload)
    yield
    # return battery in ready mode
    payload = {'Voltage': 401}
    client.post('/api/pins/5/update_pin', data=payload)


@pytest.fixture
def broke_brake_pedal():
    # set brake pedal in error mode
    payload = {'Voltage': 3}
    client.post('/api/pins/4/update_pin', data=payload)
    yield
    # return brake pedal in work mode
    payload = {'Voltage': 2}
    client.post('/api/pins/4/update_pin', data=payload)


@pytest.fixture
def pre_gear_change_pos():
    # set brake pedal in press mode
    payload = {'Voltage': 1}
    client.post('/api/pins/4/update_pin', data=payload)
    # set battery in ready mode
    payload = {'Voltage': 401}
    client.post('/api/pins/5/update_pin', data=payload)
    # set acc_pedal to 0%
    payload = {'Voltage': 1}
    client.post('/api/pins/3/update_pin', data=payload)
