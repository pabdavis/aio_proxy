
from aiohttp import web


def init_routes(app: web.Application, handler) -> None:
    router = app.router

    router.add_post('/echo', handler.proxy_request)
