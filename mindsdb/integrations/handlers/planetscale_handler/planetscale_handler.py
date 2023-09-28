from collections import OrderedDict

from mindsdb.integrations.libs.const import HANDLER_CONNECTION_ARG_TYPE as ARG_TYPE
from ..mysql_handler import Handler as MySQLHandler


class PlanetScaleHandler(MySQLHandler):
    """
    This handler handles the connection and execution of queries against PlanetScale.
    """
    name = 'planet_scale'
    
    def __init__(self, name, **kwargs):
        super().__init__(name, **kwargs)

connection_args = OrderedDict(
    user={
        'type': ARG_TYPE.STR,
        'description': 'The user name used to authenticate with the Planetscale.'
    },
    password={
        'type': ARG_TYPE.STR,
        'description': 'The password to authenticate the user with the Planetscale.'
    },
    database={
        'type': ARG_TYPE.STR,
        'description': 'The database name to use when connecting with the Planetscale.'
    },
    host={
        'type': ARG_TYPE.STR,
        'description': 'The host name or IP address of the Planetscale.'
    },
    port={
        'type': ARG_TYPE.INT,
        'description': 'The TCP/IP port of the Planetscale server. Must be an integer.'
    }
)

connection_args_example = OrderedDict(
    host='127.0.0.1',
    port=4000,
    user='root',
    password='password',
    database='database'
)
