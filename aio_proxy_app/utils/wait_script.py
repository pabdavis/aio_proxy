
from aio_proxy_app.utils.common import get_config, DEFAULT_CONFIG_PATH

if __name__ == '__main__':
    config = get_config(['-c', DEFAULT_CONFIG_PATH.as_posix()])
    # wait for other services to come up (data stores, etc)
