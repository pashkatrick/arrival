import allure
import pytest
from framework.helper import *


@allure.feature('Modules')
@allure.suite('Example')
class TestModules:

    @pytest.fixture(autouse=True)
    def init(self, restclient):
        self.client = restclient

    @allure.description('')
    @pytest.mark.parametrize('pin_voltage, battery_state', [
        (-1, 'Error'),
        (399, 'NotReady'),
        (401, 'Ready')
    ])
    def test_switch_battery_state(self, pin_voltage, battery_state):
        payload = {'Voltage': pin_voltage}
        response = self.client.post('/api/pins/5/update_pin', data=payload)
        assert response.status_code == 200
        response = self.client.get('/api/signals/5')
        assert response.json()['Value'] == battery_state

    @allure.description('')
    def test_battery_error(self, broke_battery):
        expected_signals = expected_error_signals
        expected_pins = expected_error_pins
        response_sig = self.client.get('/api/signals')
        response_pins = self.client.get('/api/pins')
        assert response_sig.json() == expected_signals
        assert response_pins.json() == expected_pins

    @allure.description('')
    def test_brake_pedal_error(self, broke_brake_pedal):
        response_req = self.client.get('/api/signals/4')
        response_gear = self.client.get('/api/signals/1')
        assert response_req.json()['Value'] == '0 Nm'
        assert response_gear.json()['Value'] == 'Neutral'
        # TODO: gear position chane unavailable
        # payload = {'Voltage': 0.67}
        # response = self.client.post('/api/pins/1/update_pin', data=payload)
        # assert 'error' in  response.json()

    @allure.description('')
    def test_gear_switch_to_drive(self, pre_gear_change_pos):
        payload = {'Voltage': 3.12}
        self.client.post('/api/pins/1/update_pin', data=payload)
        payload = {'Voltage': 0.67}
        self.client.post('/api/pins/2/update_pin', data=payload)
        response = self.client.get('/api/signals/1')
        assert response.json()['Value'] == 'Drive'

    @pytest.mark.skip(reason='bulk update doesn\'t work correctly')
    @allure.description('')
    def test_swith_gear_position(self):
        payload = {
            'Pins': [
                {
                    'PinId': 1,
                    'Voltage': 0.68
                },
                {
                    'PinId': 2,
                    'Voltage': 3.12
                }
            ]
        }
        response = self.client.post('/api/pins/update_pins', data=payload)
        assert response.status_code == 200
