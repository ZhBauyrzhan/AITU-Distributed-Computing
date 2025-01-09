from http import client
import random
import select
from threading import Thread
from time import sleep
from websockets import ConnectionClosed, ConnectionClosedError, ConnectionClosedOK
from websockets.sync.client import connect

to_sleep = False

class Client:
    def __init__(self):
        ...
    def handler(self, websocket):
        while True:
            global to_sleep
            if to_sleep:
                sleep(5)
                to_sleep = False
            try:
                message = websocket.recv()
                if message == "Send me status":
                    websocket.send('I\'m online')
                else:
                    print(f"We got message with text: {message}")
            except ConnectionAbortedError:
                print("Connection closed")
    def connect(self):
        try:
            print("WAS")
            with connect("ws://localhost:8765/") as websocket:
                self.handler(websocket)
        except ConnectionClosed:
            print("Closed on server")

def read_commands():
    while True:
        inp = input('Print the command')
        if inp == 'sleep':
            global to_sleep
            to_sleep = True

if __name__ == '__main__':
    client = Client()
    connecion = Thread(target=client.connect, name='Connection')
    inp = Thread(target=read_commands, name='Read commands')

    inp.start()
    connecion.run()
    inp.run()
    
    