import socket

PRODUCTION_HOST = [
    'merry-live',
    ]

if socket.gethostname() in PRODUCTION_HOST:
    from .production import *
else:
    from .local import *
