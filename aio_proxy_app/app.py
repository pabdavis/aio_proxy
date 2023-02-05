from pathlib import Path
from typing import (
    Optional,
    List,
)

from aiohttp import web

from aio_proxy_app.routes import init_routes
from aio_proxy_app.utils.common import init_config
from aio_proxy_app.handlers import MyHandlers

path = Path(__file__).parent


def init_app(config: Optional[List[str]] = None) -> web.Application:
    app = web.Application()

    init_config(app, config=config)

    handler = MyHandlers(app['config'])
    init_routes(app, handler)

    return app
