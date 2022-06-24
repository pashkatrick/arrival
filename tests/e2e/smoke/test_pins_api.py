import allure
import pytest
from hamcrest import *


@allure.feature('Pins')
@allure.suite('Smoke Get')
class TestPinsGetMethods:

    @pytest.fixture(autouse=True)
    def init(self, restclient):
        self.client = restclient

    @allure.description('')
    def test_pins(self):
        response = self.client.get('/api/pins')
        assert_that(response.status_code, equal_to(
            200), '/pins endpooint error')
        assert_that(response.status_code, greater_than(0), 'empty /pins data')

    @allure.description('')
    @pytest.mark.parametrize('pin_id', [1, 5])
    def test_pin_by_id(self, pin_id):
        response = self.client.get(f'/api/pins/{pin_id}')
        assert_that(response.status_code, equal_to(
            200), f'/pins/{pin_id} endpooint error')


@allure.feature('Pins')
@allure.suite('Smoke Post')
class TestPinsPostMethods:

    @pytest.fixture(autouse=True)
    def init(self, restclient):
        self.client = restclient

    @pytest.mark.skip(reason='empty data')
    @allure.description('')
    def test_update_pins_bulk(self, body):
        response = self.client.post(f'/api/pins/update_pin', data=body)
        assert_that(response.status_code, equal_to(200), 'example error')

    @pytest.mark.skip(reason='empty data')
    @allure.description('')
    def test_update_pin(self, pin_id, body):
        response = self.client.post(
            f'/api/pins/{pin_id}/update_pin', data=body)
        assert_that(response.status_code, equal_to(
            200), f'example error for pin {pin_id}')
