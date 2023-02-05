
import aiohttp
import jwt
import uuid

from multidict import CIMultiDict

from datetime import datetime, timezone


class MyHandlers:

    def __init__(self, config):
        self._config = config

    async def proxy_request(self, request):

        new_headers = CIMultiDict(request.headers)
        new_headers.add('x-my-jwt', self.generate_jwt_token(request))

        body = None
        url = 'https://postman-echo.com/post'
        payload = await request.json()
        async with aiohttp.ClientSession() as session:
            async with session.post(
                    url,
                    json=payload,
                    headers=new_headers
                    ) as resp:
                # print(resp.status)
                body = await resp.text()

        server_response = aiohttp.web.Response(
            text=body,
            status=resp.status)

        return server_response

    def generate_jwt_token(self, request):
        now_str = str(datetime.now(timezone.utc))
        payload_data = {
            "user": "username",
            "date": now_str,
            "jti": str(uuid.uuid4()),
            "iat": now_str
        }

        token = jwt.encode(
            payload=payload_data,
            key=self._config['app']['signing_key']
        )

        return token
