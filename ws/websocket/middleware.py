from django.urls import resolve
from .connection import WebSocket


def websockets(app):
    async def asgi(scope, receive, send):
        if scope["type"] == "websocket":
            scope.update({'client': tuple(['127.0.0.1', 17872])})  # define a specific port for communication?
            match = resolve(scope["raw_path"])
            await match.func(WebSocket(scope, receive, send), *match.args, **match.kwargs)
            return
        await app(scope, receive, send)
    return asgi