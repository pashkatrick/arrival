import allure
import pytest


@allure.feature('Signals')
@allure.suite('Smoke Example')
class TestSignalsGetMethods:

    @pytest.fixture(autouse=True)
    def init(self, restclient):
        self.client = restclient

    @allure.description('')
    @pytest.mark.order(0)
    @pytest.mark.dependency(name='test_signals')
    def test_signals(self):
        with allure.step('step: try to get all signals'):
            response = self.client.get('/api/signals')
        with allure.step('step: assert response data set'):
            assert response.status_code == 200
            assert len(response.json()) > 0

    @allure.description('')
    @pytest.mark.order(1)
    @pytest.mark.dependency(name='test_signal_by_id_positive', depends=['test_signals'])
    @pytest.mark.parametrize('sig_id, sig_name', [
        (1, 'GearPosition'),
        (2, 'AccPedalPos'),
        (3, 'BrakePedalState'),
        (4, 'ReqTorque'),
        (5, 'BatteryState'),
    ])
    def test_signal_by_id_positive(self, sig_id: int, sig_name: str):
        with allure.step(f'step: try to get signal by id {sig_id}'):
            response = self.client.get(f'/api/signals/{sig_id}')
            resp = response.json()
        with allure.step('step: assert response data set'):
            assert response.status_code == 200
            assert resp['SigId'] == sig_id
            assert resp['Name'] == sig_name

    @allure.description('')
    @allure.link('issue#44', name='old bug example')
    @pytest.mark.order(2)
    @pytest.mark.dependency(depends=['test_signal_by_id_positive'])
    @pytest.mark.parametrize('sig_id, status_code', [
        (6, 500)
    ])
    def test_signal_by_id_negative(self, sig_id: int, status_code: int):
        with allure.step(f'step: try to get signal by id {sig_id}'):
            response = self.client.get(f'/api/signals/{sig_id}')
        with allure.step(f'step: assert status code {status_code}'):
            assert response.status_code == status_code
