from time import sleep
from websockets import ConnectionClosed, ConnectionClosedError, ConnectionClosedOK
from websockets.sync.server import serve
import os 

class Server:
    def __init__(self):
        self.port = 8765
        self.connected = set()

    def handler(self, websocket):
        while True:
            if websocket not in self.connected:
                print("New connection araised")
                self.connected.add(websocket)
            counter = {'Online': 0, 'Offline': 0, 'Overload': 0}
            try:
                for ws in self.connected:
                    # print(ws)
                    try:
                        ws.send("Send me status")
                        message = ws.recv(timeout=1)
                        counter['Online']+=1
                    except TimeoutError:
                        counter['Overload']+=1
                    except ConnectionClosed:
                        # print(e)
                        # return
                        counter['Offline']+=1
            except RuntimeError:
                continue
            os.system('cls||clear')
            sleep(1)
            print(counter)
            sleep(1)

    def create_connection(self):
       with serve(self.handler, "localhost", self.port) as server:
           server.serve_forever()
    
if __name__ == '__main__':
    server = Server()
    server.create_connection()

