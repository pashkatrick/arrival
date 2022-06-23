import requests as req


class RestClient:

    def __init__(self, host='localhost', port=8099):
        self.host = f'http://{host}:{port}'
        self.body = dict(
            headers={'custom-header': 'example'}
        )

    def post(self, path: str, data: dict) -> req.Response:
        self.body['url'] = self.host + path
        self.body['data'] = data
        resp = req.post(**self.body)
        return resp

    def get(self, path: str) -> req.Response:
        self.body['url'] = self.host + path
        resp = req.get(**self.body)
        return resp
