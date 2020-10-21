from django.views.generic.base import TemplateView
from websocket.connection import WebSocket

class IndexView(TemplateView):
    template_name = "index.html"

async def websocket_view(socket: WebSocket):
    await socket.accept()
    while True:
        message = await socket.receive_text()
        await socket.send_text(message)