import asyncio
from websockets import ConnectionClosedOK, ConnectionClosed
from websockets.asyncio.client import connect

class Client:
    def __init__(self):
        pass
    
    async def send_message(self, websocket):
        while True:
            try:
                message = input('< ')
                if message.upper() == 'EXIT':
                    await websocket.close()
                    break
                await websocket.send(message)
                resp = await websocket.recv()
                print(f'> {resp}')
            except ConnectionClosedOK:
                print("Server closed connection")
    
    async def connect(self):
        try:
            async with connect("ws://localhost:8765/") as websocket:
                await self.send_message(websocket)
        except ConnectionClosed:
            print("Closed on client")

client = Client()
asyncio.run(client.connect())
