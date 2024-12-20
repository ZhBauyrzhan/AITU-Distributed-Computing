import asyncio
from websockets.asyncio.server import serve
 
class Server:
    def __init__(self):
        pass  

    async def handler(self, websocket):
        async for message in websocket:
            try:
                resp = str(int(message) + 1)
            except ValueError:
                resp = message.upper()
            await websocket.send(resp)
    async def create_connection(self):
        async with serve(self.handler, "localhost", 8765):
            await asyncio.get_running_loop().create_future()
            

server = Server()
asyncio.run(server.create_connection())
 