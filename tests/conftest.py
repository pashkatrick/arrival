import pytest
from os import path
from vyper import v
# import clients
from clients import restclient as rc

ROOT_DIR = path.join(path.dirname(path.abspath(__file__)), '')

option_list = (
    'host',
    'port'
)

pytest_plugins = [
    'framework.fixtures'
]

def pytest_addoption(parser):
    parser.addoption('--env', action='store', default=None)
    for option in option_list:
        parser.addoption(f'--{option}', action='store', default=None)


def setup_config(request):
    env = request.config.getoption('--env') or 'dev'
    config_name = f'config.{env}'
    config_path = path.join(ROOT_DIR, '../configs')
    config_full_path = path.join(config_path, config_name + '.yaml')
    if not path.exists(config_full_path):
        raise RuntimeError(
            f'Config file doesn\'t exist: {config_full_path}')

    v.set_config_name(config_name)
    v.set_config_type('yaml')
    v.add_config_path(config_path)
    v.read_in_config()

    for option in option_list:
        value = request.config.getoption(f'--{option}')
        if value:
            v.set(option, value)


@pytest.fixture(scope='session')
def restclient(request):
    restclient = rc.RestClient()
    return restclient
